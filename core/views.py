from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts':posts})

def detail(request, pkpost):
	post = get_object_or_404(Post, pk=pkpost)
	return render(request, 'detail.html', {'post': post})