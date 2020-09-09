from django.shortcuts import render

# Create your views here.
from blog.models import Blog,Category


def home_view(request):
    categorys = Category.objects.all()
    blogs = Blog.objects.all()
    obj = Blog.objects.filter().order_by('publishing_date')[ 0:3 ]
    anans =Blog.objects.filter(category__title=Blog.category)
    return render(request,'index.html', {'blogs' : blogs, 'categorys' : categorys, 'anans': anans,'obj': obj})
def about_view(request):
    return render(request, 'about.html' , {})

def category_detail(request, cats):
    categorys = Category.objects.all()
    blogs = Blog.objects.all()
    category_posts = Blog.objects.filter(category__title=cats)
    return render(request, 'category.html' , {'cats':cats, 'category_posts':category_posts,'blogs' : blogs, 'categorys' : categorys, })