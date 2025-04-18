from django.contrib import admin
from .models import Book, Author, Genre

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available')
    list_filter = ('available', 'genres')
    search_fields = ('title', 'author__name', 'isbn')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
