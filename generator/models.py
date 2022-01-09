from django.db import models

class Lyric(models.Model):
    content = models.TextField()