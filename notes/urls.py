from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("notes_list/", views.notes_list, name="notes-list"),
    path("note_create/", views.create, name="note-create"),
    path("note_detail/<int:note_id>", views.detail, name="note-detail"),
    path("note_update/<int:note_id>", views.update, name="note-update"),
    path("note_delete/<int:note_id>", views.delete, name="note-delete"),  # type: ignore
]
