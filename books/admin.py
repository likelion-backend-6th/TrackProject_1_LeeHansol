from django.contrib import admin

from books.models import Item


# Register your models here.

@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'available']

