from django.contrib import admin
from .models import *
# Re gister your models here.
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name' , 'email' ,'password')