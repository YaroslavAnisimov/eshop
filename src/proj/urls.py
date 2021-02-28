"""proj URL Configuration

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
from django.contrib import admin
from django.urls import path
from references.views import AuthorsList
from references import views



urlpatterns = [
    path('admin/', admin.site.urls), #http://127.0.0.1:8000/admin/
    #path('authors/', views.authors_list, name='authors-list'), 
    #path('authors/<int:pk>/', views.author_detail, name='author-detail'),
    #path('author-delete/<int:pk>/', views.author_delete, name='author-delete'),
    #path('author-create/', views.author_create, name='author-create'),
    path('authors/', views.AuthorsList.as_view (), name='authors-list'),
    path('authors-cbv/<int:pk>/', views.AuthorDetail.as_view (), name='author-detail-cbv'),
    path('author-create-cbv/', views.AuthorCreate.as_view(), name='author-create-cbv')
    path('author-delete-cbv/<int:pk>/', views.AuthorDelete.as_view, name='author-delete-cbv'),
    path('author-update/<int:pk>/', views.author_update, name='author-update'),
    
    #path('authors/<int:pk>', views.author_details)
    
    
#1.URL http://127.0.0.1:8000/cities/3/ (pk)
#2.GET http://127.0.0.1:8000/cities/?city_id=4...
#3.POST k:v, k:v  
    
    
    
    
    
]
