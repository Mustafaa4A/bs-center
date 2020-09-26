from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, auth
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    # slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='pics')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user)
