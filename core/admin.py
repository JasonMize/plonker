from django.contrib import admin

from .models import User, Post


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
    ]





class PostAdmin(admin.ModelAdmin):
    list_display = [
        'text',
        'date_added',
    ]





admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)




