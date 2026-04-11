from django import forms
from django.utils.safestring import mark_safe
from .models import Event, Favorite
from django.contrib.auth.models import User

class AttendeeChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name} ({obj.id})"  # type: ignore

class EventFormAdmin(forms.ModelForm):
    manager = forms.ModelChoiceField(
        queryset=User.objects.all().order_by("username"),
        required=False,
        label="관리자",
        empty_label="관리자 선택",
        widget=forms.Select(
            attrs={"class": "form-select", "placeholder": "관리자 선택"}
        ),
    )
    attendees = AttendeeChoiceField(
        queryset=Favorite.objects.all().order_by("-name"),
        required=False,
        label=mark_safe(
            '<span style="display: inline-block; font-size: 1rem; margin: 10px; color:red;">참석자</span>'
        ),
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
    )
    description = forms.CharField(
        required=False,
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "이벤트 설명",
                "rows": "3",
            }
        )
    )
    

    class Meta:
        model = Event
        fields = [ "title", "description", "start_date", "end_date",
            "is_completed", "manager", "attendees",
        ]
        labels = {
            "title": "",
            "start_date": "시작일시",
            "end_date": "종료일시",
            "is_completed": "완료 여부",
            "description": "",
            "attendees": "참석자",
            "manager": "관리자",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "이벤트 이름"}
            ),
            "start_date": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                    "required": "true",
                }
            ),
            "end_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "style": "margin-left: 10px;font-size: 1.2rem;",
                }
            ),
        }


class EventForm(forms.ModelForm):
    attendees = AttendeeChoiceField(
        queryset=Favorite.objects.all().order_by("-name"),
        label=mark_safe(
            '<span style="display: inline-block; font-size: 1rem; margin: 10px; color:red;">참석자</span>'
        ),
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Event
        fields = [ "title", "description", "start_date", "end_date",
            "is_completed", "attendees",
        ]
        labels = {
            "title": "",
            "description": "",
            "start_date": "시작일시",
            "end_date": "종료일시",
            "is_completed": "",
            "attendees": "참석자",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "이벤트 이름"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "이벤트 설명",
                    "rows": "3",
                }
            ),
            "start_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "end_date": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "style": "margin-left: 10px;font-size: 1.2rem;",
                }
            ),
        }


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ["name", "description", "image"]
        labels = {
            "name": "",
            "description": "",
            "image": "",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "이름",
                }
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "설명", "rows": "2"}
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "이미지",
                }
            ),
        }
