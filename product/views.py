from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from taggit.models import Tag
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request, tag_slug=None):
    object_list = Product.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    products = object_list

    return render(request, 'product/list.html', {'products': products})

