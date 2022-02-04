from statistics import quantiles
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm
from . models import Product, Cart
from django.views.decorators.csrf import csrf_exempt

def index(request):
    products = Product.objects.order_by('-id')
    cart = Cart.objects.all()
    return render(request, 'pages/index.html', {'products':products, 'cart':cart})


def cartItem(request):
    cart = Cart.objects.order_by('-id')
    return render(request, 'pages/cart.html', {'cart':cart})


@csrf_exempt
def addToCart(request):
    product_id = request.POST.get('id')
    quantity = int(request.POST.get('quantity'))
    product = Product.objects.get(id=product_id)
    if Cart.objects.filter(product=product).exists():
        cartItem = Cart.objects.get(product=product)
        cartItem.quantity = cartItem.quantity + quantity
        cartItem.save()

        return HttpResponse(product.name + ' added')
    else:
        cartItem = Cart()
        cartItem.product = product
        cartItem.quantity = quantity
        cartItem.save()

        return HttpResponse(product.name + ' new')


def sign_in(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
      
        if user is not None :
            login(request, user)
            return redirect('index')
        else:
            message = 'Такого пользователя не существует.'   
            return HttpResponse(message)
           
    else:
        return render(request, 'pages/sign_in.html')


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def sign_up(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            # messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            messages = ValidationError(list(form.errors.values()))
            return render(request, 'pages/sign_up.html', {'form':form, 'messages':messages})
           
    else:
        form = CustomUserCreationForm()
        return render(request, 'pages/sign_up.html', {'form':form})


def settings(request):
    return render(request, 'pages/settings/index.html')

def user_data(request):
    return render(request, 'pages/settings/data.html')

