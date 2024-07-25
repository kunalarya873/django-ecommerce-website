from django.shortcuts import render, get_object_or_404
from .models import Product

def get_products(request, slug):
    try:
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'products/products.html', context={'product': product})
    except Exception as e:
        print(e)
        return render(request, '404.html')  # Ensure you have a 404.html template
