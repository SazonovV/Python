from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())

from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
@login_required
def base(request, username):
    return render(request, "home1.html", {"username": username})
def signup(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form1 = UserCreationForm()
    return render(request, 'modal_window.html', {'form1': form1})



def main(request):
    form1 = UserCreationForm(request.POST)
    form = AuthenticationForm(request.POST)
    context = {'form1': form1, 'form': form, }
    return render(request, "main.html", context)


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())