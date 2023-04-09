from django import urls
from django.urls import path,include
from store import views

urlpatterns = [
    path('product_list',views.ProductListView.as_view(),name='product-list'),
]