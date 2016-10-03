from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User



class Post (models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    text = models.CharField (blank=True, max_length=139)
    date_added = models.DateTimeField(
        help_text="Posted on: ",
        default = timezone.now, null=True, blank=True 
    )

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return "{} - Posted on: {}".format(self.text, self.date_added)

    def get_absolute_url(self):
        return reverse("users:user_posts", args=[self.pk])



class Ripple (models.Model):
    original_post = models.OneToOneField(Post, null = True, blank = True)
    ripple_text = models.CharField(blank = True, max_length=139)
    ripple_date = models.DateTimeField(
        help_text="Posted on: ", 
        default = timezone.now, null=True, blank = True
    )

    class Meta:
        ordering = ['-ripple_date']

    def __str__(self):
        return "{} - Posted on: {}".format(self.ripple_text, self.ripple_date)

    def get_absolute_url(self):
        return reverse("core:index")


