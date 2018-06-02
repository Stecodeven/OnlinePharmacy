from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.post_list, name='product_list'),
    path('list/<tag_slug>/', views.post_list, name='product_list_by_tag'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search_product, name='search_product'),
]
