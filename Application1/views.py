from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import ProductForm
from .models import Product


# Create your views here.

# Sign-up view
def sign_up(request):
    if request.method == 'POST':
        formObj = SignUpForm(request.POST)
        if formObj.is_valid():
            messages.success(request, 'Account Created Successfully !!!')
            formObj.save()
    else:
        formObj = SignUpForm()
    return render(request, 'Application1/signup.html', {'form':formObj})

# Log-in view
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            formObj = AuthenticationForm(request=request, data=request.POST)
            if formObj.is_valid():
                uname = formObj.cleaned_data['username']
                upass = formObj.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!!')
                    return HttpResponseRedirect('/partner')
        else:
            formObj = AuthenticationForm()
        return render(request, 'Application1/userlogin.html', {'form':formObj})
    else:
        return HttpResponseRedirect('/partner/')

# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'Application1/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# Change password with old pass
#import pdb; pdb.set_trace()
def partner(request):
    products = Product.objects.all()

    context = {
        'products' : products
    }

    return render(request, 'Application1/partner.html', context)


def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner')
    else:
        form = ProductForm()

    context = {
        "form" : form
    }

    return render(request, 'Application1/addProduct.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(partner)

    context = {
        "form": form
    }

    return render(request, 'Application1/addProduct.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('partner')


def productDetail(request, pk):
    eachProduct = Product.objects.get(id=pk)

    context = {
        'eachProduct': eachProduct,
    }

    return render(request, 'Application1/productDetail.html', context)