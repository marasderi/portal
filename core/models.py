```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    privacy = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name='followers', blank=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    link = models.URLField(blank=True)
    hashtags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    icon = models.CharField(max_length=50, default='bi-bell')

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_chats(user):
        sent_chats = Message.objects.filter(sender=user).values('receiver').distinct()
        received_chats = Message.objects.filter(receiver=user).values('sender').distinct()
        chats = []
        for chat in sent_chats.union(received_chats):
            other_user = User.objects.get(id=chat['receiver'] or chat['sender'])
            if other_user != user:
                last_message = Message.objects.filter(
                    (Q(sender=user) & Q(receiver=other_user)) | (Q(sender=other_user) & Q(receiver=user))
                ).order_by('-created_at').first()
                chats.append({'user': other_user, 'last_message': last_message.content if last_message else ''})
        return chats

class Ad(models.Model):
    title = models.CharField(max_length=100)
    placement = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    user_type = models.CharField(max_length=50)

class SpecialContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```
