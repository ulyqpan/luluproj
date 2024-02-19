from django.shortcuts import get_object_or_404, render

from.models import Post

def home_page(request):
    latest_news = Post.objects.order_by('-created_at')[:4]
    return render(request, './primary/index.html', {'latest_news': latest_news})

def news_page(request):
    latest_news = Post.objects.order_by('-created_at')
    return render(request, './primary/news.html', {'latest_news': latest_news})

def news_detail_page(request, pk):
    news = get_object_or_404(Post, pk=pk)
    return render(request, './primary/news_detail.html', {'news': news})

def about_page(request):
    return render(request, './primary/about.html')
