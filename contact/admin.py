from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'phone',
        'email', 'created_date',
    )

    list_display_links = (
        'first_name',
    )

    ordering = (
        '-id',
    )

    list_filter = (
        'created_date',
    )

    search_fields = (
        'id', 'first_name', 'last_name', 'phone',
        'email', 'created_date',
    )

    list_max_show_all = 50
    list_per_page = 1
    