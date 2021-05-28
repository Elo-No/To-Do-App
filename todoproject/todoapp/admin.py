from django.contrib import admin
from .models import *

class ToDoItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(ToDoItem,ToDoItemAdmin)
