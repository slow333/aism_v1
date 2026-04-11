from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import datetime
from .models import Event, Favorite
from django.views.decorators.http import require_POST
from .forms import EventForm, EventFormAdmin, FavoriteForm

# 달력 만들기
from datetime import datetime  # noqa: F811
import calendar


# 이전 페이지로 이동하는 함수 ===========================================
def store_previous_page(request):
    if request.method == "GET":
        referer = request.META.get("HTTP_REFERER")
        if referer and request.path not in referer:
            request.session["previous_page"] = referer


# 전체 달력과 일정 표시
def calendars(request, year=None, month=None, filter_completed=False):
    if year is None or month is None:
        now = datetime.now()
        year = now.year
        month = now.month
    next_month = month + 1
    next_year = year
    if next_month == 13:
        next_month = 1
        next_year = year + 1
    prev_month = month - 1
    prev_year = year
    if prev_month == 0:
        prev_month = 12
        prev_year = year - 1

    # queryset = Event.objects.filter(start_date__year=year, start_date__month=month)
    queryset = Event.objects.all().order_by("start_date").order_by("is_completed")
    event_list = Event.objects.all().order_by("start_date").order_by("is_completed")

    filter_completed = "filter_completed" in request.GET
    if filter_completed:
        queryset = queryset.filter(is_completed=True)
    else:
        queryset = queryset.filter(is_completed=False)

    # HTMLCalendar 대신 python calendar 사용
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    weeks = cal.monthdayscalendar(year, month)

    context = {
        "weeks": weeks,
        "year": year,
        "month": month,
        "filtered_list": queryset,
        "event_list": event_list,
        "today": datetime.today(),
        "prev_year": prev_year,
        "prev_month": prev_month,
        "next_year": next_year,
        "next_month": next_month,
    }
    return render(request, "todos/calendar.html", context)

# favorites 사진 ===========================================================
def favorite_list(request):
    favotrites = Favorite.objects.all().order_by("-created_at", "-name")

    search_fatorites = request.GET.get("searched", "")
    if search_fatorites:
        favotrites = favotrites.filter(name__icontains=search_fatorites)

    pagenator = Paginator(favotrites, 8)
    page = request.GET.get("page")
    page_obj = pagenator.get_page(page)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "todos/favorite_list.html", context)

def favorite_detail(request, favorite_id):
    favorite = get_object_or_404(Favorite, pk=favorite_id)
    return render(request, "todos/favorite_detail.html", {"favorite": favorite})

def favorite_update(request, favorite_id):
    if not request.user.is_authenticated:
        return redirect("login")
    favorite = Favorite.objects.get(pk=favorite_id)

    store_previous_page(request)

    form = FavoriteForm(request.POST or None, request.FILES or None, instance=favorite)
    if form.is_valid():
        form.save()
        return redirect(request.session.pop("previous_page", "todos:favorite-list"))
    return render(
        request, "todos/favorite_update.html", {"favorite": favorite, "form": form}
    )

def favorite_create(request):
    if request.method == "POST":
        form = FavoriteForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("todos:favorite-list")
    else:
        form = FavoriteForm()
    return render(request, "todos/favorite_create.html", {"form": form})

def favorite_delete(request, favorite_id):
    favorite = Favorite.objects.get(pk=favorite_id)
    if request.method == "POST":
        favorite.delete()
        return redirect("todos:favorite-list")

# events ==============================================
def event_list(request):
    events = Event.objects.all().order_by("-start_date")
    search_event = request.GET.get("searched", "")
    search_is_completed = request.GET.get("is_completed", "")

    if search_is_completed:
        events = events.filter(is_completed=search_is_completed)

    if search_event:
        events = events.filter(title__icontains=search_event)

    pagenator = Paginator(events, 6)
    page = request.GET.get("page")
    page_obj = pagenator.get_page(page)

    return render(request, "todos/event_list.html", {"page_obj": page_obj})

def event_create(request):
    if not request.user.is_authenticated:
        messages.success(request, "이벤트를 생성하려면 로그인이 필요합니다.")
        return redirect("login")
    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST or None)
        else:
            form = EventForm(request.POST or None)
        if form.is_valid():
            event = form.save(commit=False)
            if not request.user.is_superuser:
                event.manager = request.user
            event.save()
            form.save_m2m()
            messages.info(request, "이벤트가 생성되었습니다.")
            return redirect("todos:event-list")
    else:
        initial = {
            'start_date': request.GET.get('date')
        }
        if request.user.is_superuser:
            form = EventFormAdmin(initial=initial)
        else:
            form = EventForm(initial=initial)
    return render(request, "todos/event_create.html", {"form": form})

def event_details(request, event_id):
    event = Event.objects.get(pk=event_id)
    store_previous_page(request)

    return render(request, "todos/event_detail.html", {"event": event})

def event_update(request, event_id):
    if not request.user.is_authenticated:
        messages.success(request, "이벤트를 수정하려면 로그인이 필요합니다.")
        return redirect("login")
    event = Event.objects.get(pk=event_id)

    store_previous_page(request)

    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect(request.session.pop("previous_page", "todos:event-list"))
    return render(request, "todos/event_update.html", {"event": event, "form": form})

def event_delete(request, event_id):
    if not request.user.is_authenticated:
        messages.success(request, "이벤트를 삭제하려면 로그인이 필요합니다.")
        return redirect("login")
    event = Event.objects.get(pk=event_id)
    event.delete()
    store_previous_page(request)

    return redirect(request.session.pop("previous_page", "todos:event-list"))

@require_POST
def event_set_complete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    is_completed = "is_completed" in request.POST

    if event.is_completed != is_completed:
        event.is_completed = is_completed
        event.save()
    return redirect(request.META.get("HTTP_REFERER", "todos:calendar"))

@require_POST
def event_set_complete_full(request, event_id):
    if not request.user.is_authenticated:
        messages.error(request, "상태를 변경하려면 로그인이 필요합니다.")
        return redirect("login")

    event = get_object_or_404(Event, pk=event_id)

    if not (
        request.user.is_superuser
        or (hasattr(event, "manager") and request.user == event.manager)
    ):
        messages.error(request, "이 이벤트의 상태를 변경할 권한이 없습니다.")
        return redirect(request.META.get("HTTP_REFERER", "todos:calendar"))

    is_completed = "is_completed" in request.POST

    if event.is_completed != is_completed:
        event.is_completed = is_completed
        event.save()
        status = "완료" if event.is_completed else "진행중"
        messages.success(
            request, f"이벤트 '{event.title}' 상태가 '{status}'(으)로 변경되었습니다."
        )
    return redirect(request.META.get("HTTP_REFERER", "todos:calendar"))

def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, "todos/event_detail.html", {"event": event})
