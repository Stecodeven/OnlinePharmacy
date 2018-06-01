from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('delete_product/<pid>', views.delete_product, name='delete_product'),
    path('sub_product/<pid>', views.sub_product, name='sub_product'),
    path('plus_product/<pid>', views.plus_product, name='plus_product'),
]
