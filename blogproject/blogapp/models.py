from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])


    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return f"{self.name} added comment on {self.post}"


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_photo = models.ImageField(null=True,blank=True)