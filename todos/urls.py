from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.calendars, name="calendar"),
    path("<int:year>/<int:month>/", views.calendars, name="calendar"),
    path("<int:year>/<int:month>/filter_completed/", views.calendars, name="calendar"),
    # events urls ==============================
    path("event_list/", views.event_list, name="event-list"),
    path("event_create/", views.event_create, name="event-create"),
    path("event_detail/<int:event_id>", views.event_detail, name="event-detail"),
    path("event_update/<int:event_id>", views.event_update, name="event-update"),
    path("event_delete/<int:event_id>", views.event_delete, name="event-delete"),  # type: ignore
    path(
        "event_set_complete/<int:event_id>",
        views.event_set_complete,
        name="event-set-complete",
    ),
    # favorite urls ==============================
    path("favorite_list/", views.favorite_list, name="favorite-list"),
    path("favorite_create/", views.favorite_create, name="favorite-create"),
    path(
        "favorite_detail/<int:favorite_id>",
        views.favorite_detail,
        name="favorite-detail",
    ),
    path(
        "favorite_update/<int:favorite_id>",
        views.favorite_update,
        name="favorite-update",
    ),
    path("favorite_delete/<int:favorite_id>", views.favorite_delete, name="favorite-delete"),  # type: ignore
]
