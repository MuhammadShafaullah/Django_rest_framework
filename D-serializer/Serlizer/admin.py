from django.contrib import admin
from .models import Studentdata
# Register your models here.

@admin.register(Studentdata)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','roll','city')
