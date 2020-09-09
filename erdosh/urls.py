"""erdosh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from blog.views import blog_detail
from home.views import home_view, about_view,category_detail

urlpatterns = [
    url(r'^adminerdo/', admin.site.urls),
    url(r'^$', home_view,name='home'),
    url(r'^index/$', home_view, ),
    url(r'^about/$', about_view),
    url(r'^category/(?P<cats>[\w-]+)/$', category_detail, name='cats'), #css is working
    url(r'^blog/(?P<slug>[\w-]+)/$', blog_detail , name= 'detay'),#css is not working
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)