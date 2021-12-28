from django.shortcuts import render
from apps.store.models import Product,Category
from apps.order.models import Order



def frontpage(request):
    products =Product.objects.filter(is_featured=True)
    featured_category=Category.objects.filter(is_featured=True)
    context={
        'products':products,
        'featured_category':featured_category
    }
    return render(request, 'frontpage.html',context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
