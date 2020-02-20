from django.contrib import admin
from .models import Author,Language,Book,BookInstance,Genre
# Register your models here.

#admin.site.register(Author)
admin.site.register(Language)
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)

#Define Admin class for All the models
class BookInline(admin.TabularInline):
    model=Book
class AuthorAdmin(admin.ModelAdmin):
    """Admin class for Author Model"""
    list_display=('last_name', 'first_name', 'date_of_birth','date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines=[BookInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    #model.extra=0

class BookAdmin(admin.ModelAdmin):
    """Admin class for Book Model"""
    list_display=('title', 'author', 'display_genre')
    inlines=[BooksInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    """Admin Class for BookInstance Model"""
    list_display=('book', 'status', 'borrower', 'due_back', 'id')
    list_filter=('status','due_back')


    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

#Register the Admin class with the associated models
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(BookInstance,BookInstanceAdmin)
