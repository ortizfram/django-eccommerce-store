from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from store.models import Product

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, "store/basket/summary.html", {"basket": basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = str(request.POST.get("productid"))
        product_qty = str(
            request.POST.get("productqty")
        )  # from frontendt script request, send to back
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({"qty": basketqty})  # no need to decoded() skey

        return response
    
def basket_delete(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = str(request.POST.get("productid"))
        product_qty = str(
            request.POST.get("productqty")
        )  # from frontendt script request, send to back
        product = get_object_or_404(Product, id=product_id)
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        response = JsonResponse({"qty": basketqty})  # no need to decoded() skey

        return response

def basket_update(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = str(request.POST.get("productid"))
        product_qty = str(
            request.POST.get("productqty")
        )  # from frontendt script request, send to back

        print(product_id)
        print(product_qty)

        response = JsonResponse({"Success": True}) 
        return response