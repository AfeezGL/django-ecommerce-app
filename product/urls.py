from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = "index" ),
    path('add-to-cart/', views.add_to_cart, name = "add_to_cart"),
    path('cart', views.CartView, name = "cart" ),
    path('product/showcase/<int:pk>/', views.ProductDetailView.as_view(), name="details"),
]