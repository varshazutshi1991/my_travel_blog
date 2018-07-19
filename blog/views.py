from django.shortcuts import render
from blog.models import Blogger, Blog


# Create your views here.


def blog_list(request):
    template = 'blog/blog_list.html'
    return render(request, template, {})

def homepage(request):
    template = 'blog/homepage.html'
    blog_details = Blog.objects.all()
    blog_detail_list = Blog.objects.order_by('-travel_date')[:5]
    output = ', '.join([q.title for q in blog_detail_list])
    return render(request, template, {'blog_details': blog_details, 'output': output, 'blog_detail_list': blog_detail_list})


def blog_detail(request, blog_id):
    template = 'blog/blog_details.html'
    blog_detail_list = Blog.objects.order_by('-travel_date')[:5]
    output = ', '.join([q.title for q in blog_detail_list])
    return render(request, template, {'output': output, 'blog_detail_list':blog_detail_list})
