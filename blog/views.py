from django.shortcuts import render, get_object_or_404

# Create your views here
from blog.models import Blog


def blog_detail(request, slug):
    detay = get_object_or_404(Blog, slug=slug)
    context = {
        'blog': detay,
    }
    return render(request, 'post/detay.html', context)



