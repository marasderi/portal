```python
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
from django.db.models import Q

def search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        # Kullanıcı arama
        users = User.objects.filter(username__icontains=query)
        for user in users:
            results.append({'type': 'user', 'id': user.id, 'username': user.username})

        # Gönderi arama (içerik ve hashtag’ler)
        posts = Post.objects.filter(
            Q(content__icontains=query) | Q(hashtags__icontains=query)
        ).distinct()
        for post in posts:
            results.append({'type': 'post', 'id': post.id, 'content': post.content})

        # Etiket arama (sadece hashtag’leri ayırarak)
        hashtags = set()
        for post in Post.objects.all():
            if query.lower() in post.hashtags.lower():
                hashtags.update(post.hashtags.split())
        for hashtag in hashtags:
            if query.lower() in hashtag.lower():
                results.append({'type': 'hashtag', 'hashtag': hashtag})

    return render(request, 'core/search.html', {'query': query, 'results': results})
```
