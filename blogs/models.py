from django.conf import settings
from django.db import models


class Post(models.Model):
    """ blog post
    """
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=300, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    tags = models.CharField(max_length=200)

    archive = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

        
