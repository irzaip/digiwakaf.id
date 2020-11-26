from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .models import *
from .forms import *
from .filter import *
from .decorators import *

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            fullname = str(form.cleaned_data.get('first_name')) + str(form.cleaned_data.get('lastname'))

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            Customer.objects.create(
                user=user,
            )
            messages.success(request,"Account created successfully")
            return redirect('login')
        else:
            return HttpResponse("Error creating new user -> check user and password requirements")

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@authdUser
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request,'Username or Password INCORRECT!')

    
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')


def homePage(request):
    user = request.user
    assets = Asset.objects.all()
    context = {'assets': assets, 'user': user}
    return render(request, 'account/home.html', context)

def assetPage(request, pid):
    product = Asset.objects.get(id=pid)
    context = {'product': product}
    return render(request, 'account/products.html', context)

def lookupassetPage(request, pid):
    product = Asset.objects.get(id=pid)
    context = {'product': product}
    return render(request, 'account/products.html', context)

def customer(request):
    context = {}
    return render(request, 'account/customer.html', context)