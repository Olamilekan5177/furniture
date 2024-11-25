from django.shortcuts import render

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
  return render(request, 'myapp/index.html')

def services(request):
  return render(request, 'myapp/services.html')

def shop(request):
  return render(request, 'myapp/shop.html')

def thankyou(request):
  return render(request, 'myapp/thankyou.html')
