from django.contrib import admin
from apps.author.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'nationality', 'birth_date', 'get_age']
    list_display_links = ['full_name']
    list_filter = ['nationality']
    search_fields = ['full_name', 'nationality']
    ordering = ['first_name']
    # readonly_fields = ['views']


admin.site.register(Author, AuthorAdmin)