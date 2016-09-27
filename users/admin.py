from django.contrib import admin

from .models import Post


# class UserAdmin(admin.ModelAdmin):
#     list_display = [
#         'name', 
#     ]





class PostAdmin(admin.ModelAdmin):
    list_display = [
        # 'user',
        'text',
        'date_added',
    ]





# admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
