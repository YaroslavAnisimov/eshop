from django.urls import path
from cart import views


app_name = 'cart'

urlpatterns = [
    path('add-to-cart/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('view-cart/', views.CartView.as_view(), name='view-cart'),
    path('update-cart/', views.UpdateCart.as_view(), name='update-cart'),
    path('delete-from-cart/<int:pk>/', views.DeleteFromCart.as_view(), name='delete-from-cart'),
]


# from django.urls import path
# from . import views

# app_name = 'cart'

# urlpatterns = [
#     path('add-to-cart/', views.UpdateCart.as_view(), name="add-to-cart"),
#     path('recalculate-cart/', views.RecalculateCart.as_view(), name="recalculate-cart")
# ]

