"""BlablaChinese1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from website import views
from .views import AddPostView, UpdatePostView, DeletePostView, BlogView, BlogDetailView, AddCategoryView

urlpatterns = [
    path('', views.home, name='home'),
    # path('blog/', views.blog, name='blog'),
    path('blog/', BlogView.as_view(), name='blog'),
    # path('blog/<str:slug>', views.blogpost, name='blogpost'),
    path('blog/<str:slug>', BlogDetailView.as_view(), name='blogpost'),
    path('categories/<str:cats>', views.Categories, name='categories'),
    path('tags/<str:tag>', views.Tags, name='tags'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('blog/edit/<str:slug>', UpdatePostView.as_view(), name='update-post'),
    path('blog/<str:slug>/delete', DeletePostView.as_view(), name='delete-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),


]
