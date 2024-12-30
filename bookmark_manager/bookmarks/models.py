from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title
