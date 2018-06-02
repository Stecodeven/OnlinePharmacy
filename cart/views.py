from product.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect, reverse
import redis
from django.conf import settings
# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB,
                      password=settings.REDIS_PASSWORD)


def update_session(request, cart_key):
    total_price = 0
    cart_dict = r.hgetall(cart_key)
    for p_id, count in cart_dict.items():
        sku = get_object_or_404(Product, id=p_id, available=True)
        amount = sku.price * int(count)
        total_price += amount
    request.session["total_price"] = float(total_price)
    request.session.set_expiry(0)


@login_required
def add_product(request):
    p_id = request.POST.get('p_id')
    count = request.POST.get('count')

    count = int(count)
    origin_count = count

    cart_key = 'cart_%d' % request.user.id
    cart_count = r.hget(cart_key, p_id)

    # 如果用户买过该商品，直接在之前的数量上添加，没有买过，那么建立相应的键值对。
    if cart_count:
        # 商品数目累加
        count += int(cart_count)
    r.hset(cart_key, p_id, count)


    # 获取总价
    if 'total_price' in request.session:
        sku = get_object_or_404(Product, id=p_id, available=True)
        request.session["total_price"] = request.session["total_price"] + float(sku.price) * int(origin_count)
    else:
        update_session(request, cart_key)

    # session更新完毕

    # 返回应答
    return JsonResponse({'cart_count': request.session["total_price"], 'message': '添加成功'})


@login_required
def cart_detail(request):

    user = request.user

    cart_key = 'cart_%d' % user.id
    cart_dict = r.hgetall(cart_key)  # {'sku_id':商品数量}

    products = []
    total_count = 0
    total_price = 0
    # 获取购物车中商品id对应的商品信息
    for p_id, count in cart_dict.items():
        # 根据sku_id获取商品的信息
        sku = get_object_or_404(Product, id=p_id, available=True)
        # 计算商品的小计
        amount = sku.price * int(count)
        # 动态给sku对象增加属性amount和count, 分别保存商品的小计和购物车中商品的数量
        sku.amount = amount
        sku.count = int(count)
        # 添加sku
        products.append(sku)
        # 累加计算商品的总件数和总价格
        total_count += int(count)
        total_price += amount

    return render(request, 'cart/detail.html', {'total_count': total_count, 'total_price': total_price,
                                                'products': products})


@login_required
def delete_product(request, pid):
    user = request.user

    cart_key = 'cart_%d' % user.id
    count = r.hget(cart_key, pid)
    print(count)
    r.hdel(cart_key, pid)
    sku = get_object_or_404(Product, id=pid, available=True)

    if 'total_price' in request.session:
        request.session["total_price"] = request.session["total_price"] - float(sku.price) * int(count)
    else:
        update_session(request, cart_key)
    return redirect(cart_detail)


@login_required
def sub_product(request, pid):
    user = request.user

    cart_key = 'cart_%d' % user.id
    cart_count = r.hget(cart_key, pid)
    if int(cart_count) == 1:
        return redirect(delete_product, pid)

    r.hset(cart_key, pid, int(cart_count)-1)
    sku = get_object_or_404(Product, id=pid, available=True)

    if 'total_price' in request.session:
        request.session["total_price"] = request.session["total_price"] - float(sku.price)
    else:
        update_session(request, cart_key)
    return redirect(cart_detail)


@login_required
def plus_product(request, pid):
    user = request.user

    cart_key = 'cart_%d' % user.id
    cart_count = r.hget(cart_key, pid)

    r.hset(cart_key, pid, int(cart_count)+1)
    sku = get_object_or_404(Product, id=pid, available=True)

    if 'total_price' in request.session:
        request.session["total_price"] = request.session["total_price"] + float(sku.price)
    else:
        update_session(request, cart_key)
    return redirect(cart_detail)






