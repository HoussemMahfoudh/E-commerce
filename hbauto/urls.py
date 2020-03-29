
from django.contrib import admin
from django.urls import path, include

name_space = 'admin'


urlpatterns = [
    path('admin/', admin.site.urls, name='adminspace'),
    path('',include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('cart/',include('cart.urls')),
    path('',include('products.urls')),
    
]
