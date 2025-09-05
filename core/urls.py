```python
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('search/', views.search, name='search'),
    path('notifications/', views.notifications, name='notifications'),
    path('messages/<int:receiver_id>/', views.messages, name='messages'),
    path('discover/', views.discover, name='discover'),
    path('settings/', views.settings, name='settings'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('hashtag/<str:hashtag>/', views.hashtag, name='hashtag'),
    path('followers/', views.followers, name='followers'),
    path('special-content/', views.special_content, name='special_content'),
    path('ads/', views.ads, name='ads'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('about/', views.about, name='about'),
]
```
