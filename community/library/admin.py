from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author')
    list_filter = ('category',)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Category)
