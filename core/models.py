from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class User (models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ("users:user_posts", args=[self.pk])



class Post (models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(
        help_text="Posted on:",
        default = timezone.now, null=True, blank=True
    )
    user = models.ForeignKey("User", null=True, blank=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return "{} - Posted on: {}".format(self.text, self.date_added)

    def get_absolute_url(self):
        return reverse("users:user_posts", args=[self.pk])









