from django.contrib import admin

from .models import Post, Ripple



class PostAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date_added',
        'text',
    ]

class RippleAdmin (admin.ModelAdmin):
    list_display = [
        'original_post',
        'original_post_owner',
    ]



admin.site.register(Post, PostAdmin)
admin.site.register(Ripple, RippleAdmin)

