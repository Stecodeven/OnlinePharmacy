from django.shortcuts import render


def order_index(request):
    #if request.method == 'POST':
    valuelist = request.POST.getlist("if_buy")
    for i in valuelist:
        print(i,"dsada")
    print("dsadasd")
    return render(request, 'order_detail.html')
