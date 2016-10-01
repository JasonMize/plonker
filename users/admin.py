from django.contrib import admin

from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date_added',
        'text',
        
    ]




admin.site.register(Post, PostAdmin)


