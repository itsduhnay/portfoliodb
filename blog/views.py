from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

def blog_index(request):
    blogs = Blog.objects.all().order_by('-pub_date')
    return render(request, 'blog/bloglist.html', {"blogs":blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
