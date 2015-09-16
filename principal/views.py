from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from principal.models import Post
from django.http import HttpResponse


def index(request):
    posts = Post.objects.get(id=1)
    points = posts.location
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user,
                              'qs_results': points})
    return render_to_response('index.html', context_instance=context)


