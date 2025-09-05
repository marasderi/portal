from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Profile, Follow, Message, SpecialContent, Ad
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    return render(request, 'core/home.html', {'posts': posts})

@login_required
def profile(request):
    return render(request, 'core/profile.html')

def user_profile(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    is_following = Follow.objects.filter(follower=request.user, followed=profile_user).exists()
    return render(request, 'core/user_profile.html', {'profile_user': profile_user, 'is_following': is_following})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'core/post_detail.html', {'post': post})

@login_required
def follow(request, user_id):
    if request.method == 'POST':
        followed = get_object_or_404(User, id=user_id)
        follow, created = Follow.objects.get_or_create(follower=request.user, followed=followed)
        if not created:
            follow.delete()
        return HttpResponseRedirect(reverse('core:user_profile', args=[user_id]))
    return redirect('core:home')

# Diğer görünümler (arama, mesajlar, vb.) benzer şekilde tanımlanır.
