from django import forms
from django.utils.safestring import mark_safe
from .models import Note
from django.contrib.auth.models import User

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "description", "writer", "is_completed",)
        labels = {
            "title": "",
            "description": "",
            "created_at": "작성일",
            "writer": "작성자",
            "is_completed": "완료 ",
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
            "created_at": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                    "style": "margin-left: 10px;font-size: 1.2rem;",
                }
            ),
        }
