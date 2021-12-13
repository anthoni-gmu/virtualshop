from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from apps.cart.cart import Cart



def product_detail(request,category_slug, slug):
    product=get_object_or_404(Product,slug=slug)
    cart=Cart(request)
    
    context={
        'product':product,
        'cart':cart,
        
    }
    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category=get_object_or_404(Category,slug=slug)
    cart=Cart(request)
    
    products=category.products.filter(is_featured=True)
    context={
        'category':category,
        'products':products,
        'cart':cart,
        
               
    }
    return render(request, 'category_detail.html', context)
    