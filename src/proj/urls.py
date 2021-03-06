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
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views as main_views
from references import urls as refs_urls
from users import urls as users_urls
from cart import urls as cart_urls


#from references.views import books_list
# from cart import views as cart_views


urlpatterns = [
    path('admin/', admin.site.urls), #http://127.0.0.1:8000/admin/
    path('', main_views.HomePage.as_view(), name='homepage'),
    path('books-catalog', main_views.BooksCatalog.as_view(), name='books-catalog'),
    path('references/', include(refs_urls, namespace='references')),
    path('users/', include(users_urls, namespace='users')),
    path('cart/', include(cart_urls, namespace='cart')),
    # path('books/', ref_views.BooksList.as_view(), name='books-list'),
    # path('books/<int:pk>/', ref_views.BookDetail.as_view(), name='book-detail'),
    # path('book-delete/<int:pk>/', ref_views.BookDelete.as_view(), name='book-delete'),
    # path('book-create/', ref_views.BookCreate.as_view(), name='book-create'),
    # path('book-update/<int:pk>/', ref_views.BookUpdate.as_view(),name="book-update"),
    # path('accs/', include(accs_urls)), 
    # path('cart/', include(cart_urls, namespace="cart")),
    # path('cart/', cart_views.HomePage.as_view(), name = "home-page")
    # path('home', ref_views.HomeList.as_view(), name='home'),
    # path('books/', views.books_list, name='books_list'), 
    # path('books/<int:pk>/', views.book_detail, name='book-detail'),
    # path('book-delete/<int:pk>/', views.book_delete, name='book-delete'),
    # path('book-create/', views.book_create, name='book-create'),
    # path('book-update/<int:pk>/', views.book_update, name='book-update'), 
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings .MEDIA_ROOT)  

    #path('books/<int:pk>', views.book_details)
    
    
#1.URL http://127.0.0.1:8000/cities/3/ (pk)
#2.GET http://127.0.0.1:8000/cities/?city_id=4...
#3.POST k:v, k:v    

