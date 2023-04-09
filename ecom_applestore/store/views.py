from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView

from store.models import Products


# Create your views here.


class ProductListView(ListView):
    model = Products
    context_object_name="products"
    template_name = "product-list.html"
    


