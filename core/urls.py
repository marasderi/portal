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
    # Diğer URL'ler burada kalabilir
]
```
