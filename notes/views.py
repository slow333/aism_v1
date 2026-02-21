from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

def notes_list(request):
    notes = Note.objects.all().order_by("-created_at")
    search_note = request.GET.get("searched", "")
    search_is_completed = request.GET.get("is_completed", "")

    if search_is_completed:
        notes = notes.filter(is_completed=search_is_completed)

    if search_note:
        notes = notes.filter(title__icontains=search_note)

    pagenator = Paginator(notes, 6)
    page = request.GET.get("page")
    page_obj = pagenator.get_page(page)

    return render(request, "notes/notes_list.html", {"page_obj": page_obj})

@login_required
def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST or None)
        if form.is_valid():
            note = form.save(commit=False)
            note.writer = request.user
            note.save()
            form.save_m2m()
            messages.info(request, "이벤트가 생성되었습니다.")
            return redirect("notes:notes-list")
    form = NoteForm()
    return render(request, "notes/create.html", {"form": form})

def detail(request, note_id):
    note = Note.objects.get(pk=note_id)
    return render(request, "notes/detail.html", {"note": note})

@login_required
def update(request, note_id):
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST or None, instance=note)
        if form.is_valid():
            form.save()
        return redirect("notes:notes-list")
    form = NoteForm(instance=note)
    return render(request, "notes/update.html", {"note": note, "form": form})

@login_required
def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect("notes:notes-list")
