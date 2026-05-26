from django.shortcuts import render
from bangazonapi.models import Product
from bangazonapi.views import ProductSerializer

def reports(request):
    return render(request, 'bangazonapi/reports_base.html')

def expensiveproducts(request):
    products = Product.objects.filter(price__gt=1000)
    context = {
        "product_list": products
    }
    return render(request, 'bangazonapi/expensiveproducts.html', context=context)