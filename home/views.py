from django.shortcuts import render, Http404
from .models import News


def index(request):
    articles = News.objects.all()
    return render(request, 'home/index.html', locals())


def article(request, i):
    try:
        new = News.objects.get(id=i)
    except News.DoesNotExist:
        raise Http404
    return render(request, 'home/article.html', locals())