from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<tag_slug>/', views.post_list, name='post_list_by_tag'),
]
