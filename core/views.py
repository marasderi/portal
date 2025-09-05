```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Post, Comment, Notification, Message, Profile, Ad, SpecialContent

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, user=request.user, content=content)
            return redirect(reverse('core:post_detail', args=[post_id]))
    return render(request, 'core/post_detail.html', {'post': post})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/notifications.html', {'notifications': notifications})

@login_required
def messages(request, receiver_id=None):
    chats = Message.get_chats(request.user)
    messages = []
    receiver = None
    if receiver_id:
        receiver = get_object_or_404(User, id=receiver_id)
        messages = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver=receiver)) | 
            (Q(sender=receiver) & Q(receiver=request.user))
        ).order_by('created_at')
    if request.method == "POST":
        content = request.POST.get('content')
        if content and receiver:
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return redirect(reverse('core:messages', args=[receiver_id]))
    return render(request, 'core/messages.html', {'chats': chats, 'messages': messages, 'receiver': receiver, 'user': request.user})

@login_required
def discover(request):
    trend_posts = Post.objects.order_by('-likes_count')[:5]  # Örnek trend hesaplama
    trends = set()
    for post in Post.objects.all():
        trends.update(post.hashtags.split())
    return render(request, 'core/discover.html', {'trend_posts': trend_posts, 'trends': trends})

@login_required
def settings(request):
    if request.method == "POST":
        bio = request.POST.get('bio')
        if request.FILES.get('profile_picture'):
            request.user.profile.profile_picture = request.FILES['profile_picture']
        request.user.profile.bio = bio
        request.user.profile.privacy = 'privacy' in request.POST
        request.user.profile.save()
        return redirect(reverse('core:settings'))
    return render(request, 'core/settings.html', {'user': request.user})

@login_required
def post_create(request):
    if request.method == "POST":
        content = request.POST.get('content')
        link = request.POST.get('link')
        hashtags = request.POST.get('hashtags')
        if content:
            Post.objects.create(user=request.user, content=content, link=link, hashtags=hashtags)
            return redirect(reverse('core:home'))
    return render(request, 'core/post_create.html', {'post': None})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        content = request.POST.get('content')
        link = request.POST.get('link')
        hashtags = request.POST.get('hashtags')
        if content:
            post.content = content
            post.link = link
            post.hashtags = hashtags
            post.save()
            return redirect(reverse('core:post_detail', args=[post_id]))
    return render(request, 'core/post_create.html', {'post': post})

@login_required
def hashtag(request, hashtag):
    posts = Post.objects.filter(hashtags__icontains=hashtag)
    return render(request, 'core/hashtag.html', {'hashtag': hashtag, 'posts': posts})

@login_required
def followers(request):
    following = request.user.profile.following.all()
    followers = request.user.profile.followers.all()
    return render(request, 'core/followers.html', {'following': following, 'followers': followers})

@login_required
def special_content(request):
    special = SpecialContent.objects.filter(user=request.user).first()
    return render(request, 'core/special_content.html', {'special': special})

@login_required
def ads(request):
    ads = Ad.objects.all()
    return render(request, 'core/ads.html', {'ads': ads})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('core:home'))
    return render(request, 'core/login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'core/login.html', {'error': 'Kullanıcı adı alınmış.'})
        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user)
        login(request, user)
        return redirect(reverse('core:home'))
    return render(request, 'core/login.html')

def password_reset(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # E-posta gönderme mantığı buraya eklenecek (örneğin, Django'nun built-in password reset view’ı)
        return redirect(reverse('core:login'))
    return render(request, 'core/password_reset.html')

def about(request):
    return render(request, 'core/about.html')
```
