from django.shortcuts import get_object_or_404, render
from .import models
from category.models import Category

# Create your views here.


def store(request , category_slug = None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category , slug = category_slug)
        products = models.Product.objects.filter(category = categories , is_available = True)
        product_counts = products.count()
    else:
        products = models.Product.objects.all().filter(is_available = True)
        product_counts = products.count()
    
    context = {
        'products': products,
        'product_counts' : product_counts
    }
    return render(request, 'store/store.html' , context)