from django.shortcuts import render
from .models import Product, Product2

# Create your views here.
def base(request):
  return render(request, 'myapp/base.html')

def about(request):
  return render(request, 'myapp/about.html')

def blog(request):
 
  return render(request, 'myapp/blog.html')

def cart(request):
  return render(request, 'myapp/cart.html')

def checkout(request):
  return render(request, 'myapp/checkout.html')

def contact(request):
  return render(request, 'myapp/contact.html')

def index(request):
  products = Product.objects.all()
  return render(request, 'myapp/index.html', {'products': products})

def services(request):
  products = Product.objects.all()
  return render(request, 'myapp/services.html', {'products': products})


def shop(request):
    product2s = Product2.objects.all()
    return render(request, 'myapp/shop.html', {'product2s': product2s})

def thankyou(request):
  return render(request, 'myapp/thankyou.html')
