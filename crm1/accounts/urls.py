from django.urls import path

from .views import index, customer, products


urlpatterns = [
    path('', index, name='index'),
    path('customer', customer, name='customer'),
    path('products', products, name='products')
]