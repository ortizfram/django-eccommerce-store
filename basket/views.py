from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from store.models import Product

from .basket import Basket

def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty')) # from frontendt script request, send to back
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        response = JsonResponse({'qty': product_qty}) # no need to decoded() skey

        return response