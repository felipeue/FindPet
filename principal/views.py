from django.shortcuts import render
from principal.models import Post


def index(request):
    points = Post.objects.all()
    return render(request, 'index.html', {'points': points})


