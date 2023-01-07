from django.contrib import admin
from apps.book.models import Category, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published', 'views']
    list_display_links = ['title']
    list_filter = ['category', 'published']
    search_fields = ['title', 'category']
    ordering = ['title']
    # readonly_fields = ['views']


admin.site.register(Category)
admin.site.register(Book, BookAdmin)