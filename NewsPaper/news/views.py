from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    news = Post.objects.all()
    return render(request, 'news/news_list.html', {'posts': news})

def news_detail(request, id):
    news_item = get_object_or_404(Post, pk=pk)
    return render(request, 'news/news_detail.html', {'post': news_item})