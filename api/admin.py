from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'fathers_name')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoy_name',)
    search_fields = ('categoy_name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'book_title',)
    search_fields = ('book_title',)
    list_filter = ('category',)

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
