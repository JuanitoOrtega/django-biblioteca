from django.contrib import admin
from apps.reader.models import Reader, Lend


class ReaderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'nationality', 'birth_date', 'get_age']
    list_display_links = ['full_name']
    list_filter = ['nationality']
    search_fields = ['full_name', 'nationality']
    ordering = ['first_name']
    # readonly_fields = ['views']


class LendAdmin(admin.ModelAdmin):
    list_display = ['book', 'reader', 'lend_date', 'return_date', 'returned']
    list_display_links = ['book']
    list_filter = ['book', 'reader', 'lend_date', 'returned']
    search_fields = ['book', 'reader']
    ordering = ['book']
    # readonly_fields = ['views']


admin.site.register(Reader, ReaderAdmin)
admin.site.register(Lend, LendAdmin)