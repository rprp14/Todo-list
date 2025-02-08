from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'description')  # Fields to display in the list view
    list_filter = ('status','completed')  # Add filter by status
    search_fields = ('title', 'description')  # Make title and description searchable

# Register the custom TaskAdmin class
admin.site.register(Task, TaskAdmin)
