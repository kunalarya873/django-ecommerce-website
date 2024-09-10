import contextlib
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import logging
from .models import *
logger = logging.getLogger(__name__)

def get_products(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}    
    if request.GET.get('size'):
        size = request.GET.get('size')
        price = Product.get_products_by_size(size)
        print(price)
        context['selected_size'] = size
        context['updated_price'] =price
    return render(request, 'product/product.html', context=context)    



def update_price(request):
    print("update_price view is called")  # Debugging print statement
    if size := request.GET.get('size'):
        try:
            size_variant = SizeVariant.objects.get(size_name=size)
            product = Product.objects.filter(size_variant=size_variant).first()
            if product:
                updated_price = product.get_products_by_size(size)
                return JsonResponse({'price': updated_price})
        except SizeVariant.DoesNotExist:
            pass
    return JsonResponse({'price': 'N/A'}, status=404)