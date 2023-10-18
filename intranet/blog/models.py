from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_file = models.FileField(upload_to='text_files/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video")

    def __str__(self):
        return self.caption