from django.shortcuts import render
from .cart import Cart
from django.conf import settings
def cart_detail(request):
    cart=Cart(request)
    productsstring =''
    
    for item in cart:
        product=item['product']
        b="{'id': '%s','title': '%s','price': '%s','quantity': '%s','total_price': '%s'},"%(product.id,product.title,item['price'],item['quantity'],item['total_price'])
        productsstring=productsstring+b
        
    context={
        'cart':cart,
        'productsstring':productsstring,
        'pub_key':settings.STRIPE_API_KEY_PUBLISHABLE,
    }
    return render(request, 'cart.html',context)

def success(request):
    cart=Cart(request)
    
    cart.clear()
    return render(request, 'success.html')