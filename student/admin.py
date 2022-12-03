from django.contrib import admin

from .models import User,Blogs
# Register your models here.
@admin.register(Blogs)
class UserAdmin(admin.ModelAdmin):
    list_display=["title","category","description","user"]

