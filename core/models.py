from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=[('standard', 'Standart'), ('premium', 'Premium'), ('super', 'Süper Üye')])

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Taslak'), ('published', 'Yayınlandı'), ('archived', 'Arşivlendi')])
    hashtags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:50]}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Complaint(models.Model):
    complainant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Beklemede'), ('resolved', 'Çözüldü'), ('dismissed', 'Reddedildi')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Şikayet #{self.id} by {self.complainant.username}"

class Ad(models.Model):
    title = models.CharField(max_length=100)
    placement = models.CharField(max_length=50, choices=[('homepage', 'Ana Sayfa'), ('sidebar', 'Kenar Çubuğu'), ('post', 'Gönderi')])
    status = models.CharField(max_length=20, choices=[('active', 'Aktif'), ('paused', 'Duraklatıldı'), ('expired', 'Süresi Doldu')])
    user_type = models.CharField(max_length=20, choices=[('standard', 'Standart'), ('premium', 'Premium'), ('super', 'Süper Üye')])

    def __str__(self):
        return self.title

class SpecialContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50, choices=[('poll', 'Anket'), ('story', 'Hikaye')])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
