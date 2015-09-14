from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse


def index(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('index.html', context_instance=context)


