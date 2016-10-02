from django import forms

from .models import Post
from core.forms import BootstrapFormMixin


class CreatePostForm (BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text',)
        widgets = {
            'text' : forms.Textarea
                (attrs=
                    {'maxlength': '139',}
                )
        }
        labels = {
            'text' :  'Text - maximum of 139 characters',
        }
            









