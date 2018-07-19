from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.blog_list, name='blog_list'),
    path('', views.homepage, name='homepage'),
    path('/blog/<int:blog_id/>', views.blog_detail, name='blog_detail')
]



