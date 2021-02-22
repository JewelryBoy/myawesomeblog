from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=300)
    post_date = models.DateTimeField()
    post_text = models.TextField()
    event_image = models.ImageField(upload_to='post_image/')
