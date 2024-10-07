from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    
    def __str__(self) -> str:
        return self.username
    
    
# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField()
    published_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.post}'
    
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username