from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'phone',
        'email', 'created_date', 'category',
    )

    list_display_links = (
        'first_name',
    )

    ordering = (
        '-id',
    )

    list_filter = (
        'created_date', 'category',
    )

    search_fields = (
        'id', 'first_name', 'last_name', 'phone',
        'email', 'created_date', 'category',
    )

    list_max_show_all = 50


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    ordering = ('-id',)
    search_fields = ('name',)
    list_max_show_all = 50
