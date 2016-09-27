from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class User (models.Model):
    name = models.CharField(max_length=40)

class Post (models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(
        help_text="Posted on:",
        default = timezone.now, null=True, blank=True
    )
