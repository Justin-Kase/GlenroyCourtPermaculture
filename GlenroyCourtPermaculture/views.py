from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    #return HttpResponse('index.html')
     return render(request, 'index.html')

def individual_post(request):
    recent_post = Post.objects.get(id__exact=1)
    return HttpResponse(recent_post.title + ': ' + recent_post.content)

