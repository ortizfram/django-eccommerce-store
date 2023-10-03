from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from store.models import Product

from .basket import Basket
from decimal import Decimal 

def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        
        # Convert the Decimal value to float before creating the JSON response
        response_data = {'test': 'data', 'price': float(product.price)}
        response = JsonResponse(response_data)
        return response