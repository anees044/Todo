from django.contrib import admin
from .models import Tasks

class Admintask(admin.ModelAdmin):
    
    list_display=('taskname','is_completed','modifiedat')
    search_fields=('taskname',)

admin.site.register(Tasks,Admintask)
