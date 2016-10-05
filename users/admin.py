from django.contrib import admin

from .models import Post, Ripple



class PostAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date_added',
        'text',
    ]

class RippleAdmin (admin.ModelAdmin):
    list_display = (
        'original_post',
        'ripple_text', 
        'ripple_date',
    )
    list_filter = ('original_post',)



admin.site.register(Post, PostAdmin)
admin.site.register(Ripple, RippleAdmin)

