from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request, tag_slug=None):
    object_list = Product.objects.all()
    # tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    products = object_list

    choice = request.GET.get('mode') or 0
    if int(choice) == 1:
        products = products.order_by('price')
    elif int(choice) == 2:
        products = products.order_by('-sales')

    paginator = Paginator(products, 3)

    page = request.GET.get('page') or 1
    if int(page) <= 0:
        page = 1
    elif int(page) > paginator.num_pages:
        page = paginator.num_pages

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'product/list.html', {'page': page, 'products': products, 'mode': choice})


def search_product(request):
    if request.method == 'POST':
        content = request.POST['index_none_header_sysc']
        print(content)
        products = Product.objects.filter(tags__name__in=[content])
        products = products | Product.objects.filter(name__icontains=content)
        products = products | Product.objects.filter(brand__icontains=content)
        return render(request, 'product/list.html', {'products': products.distinct()})

    return render(request, 'product/list.html')


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request, 'product/detail.html', {'p': product, 'pid': product.id})





