from django import forms

from .models import Post, Ripple
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
            'text' :  'Text - 139 character maximum',
        }
            



class CreateRippleForm (BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Ripple
        fields = (
            'ripple_text', 
            'original_post',
        )
        widgets = {
            'ripple_text' : forms.Textarea
                (attrs=
                    {'maxlength': '139',}
                ),
            'original_post' : forms.HiddenInput(),   
        }
        labels = {
            'ripple_text' :  'Text - 139 character maximum',
        }


