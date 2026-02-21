from django.contrib import admin
from notes.models import Note
from django.contrib.auth.models import User

@admin.register(Note)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','created_at', 'is_completed', 'writer',)
    autocomplete_fields = ('writer',)
    list_filter = ('is_completed', )
    ordering = ('-created_at',)
    list_select_related = ('writer',)
    search_fields = ('writer','title',)
