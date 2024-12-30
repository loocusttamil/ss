from django.contrib import admin
from .models import api

@admin.register(Relay)
class RelayAdmin(admin.ModelAdmin):
    list_display = ('relay_id', 'status')  # Columns to display in the admin panel
    list_editable = ('status',)  # Allow inline editing of the status
    list_filter = ('status',)  # Add a filter for the status column
    search_fields = ('relay_id',)  # Add a search box for relay IDs
