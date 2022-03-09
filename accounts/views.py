from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import auth
from .models import *
import json
from store.utils import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data['username']
        phone_or_email = data['phoneOrEmail']
        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse('Username is already taken')
            elif Customer.objects.filter(phone_or_email=phone_or_email).exists():
                return HttpResponse('Phone number or email is already taken')
            else:
                user = User.objects.create_user(username=username, password=password1)
                Customer.objects.create(user=user, phone_or_email=phone_or_email)

                user = auth.authenticate(username=username, password=password1)
                if user is not None:
                    auth.login(request, user)
                else:
                    return HttpResponse('User was not created or does not exist')

                return HttpResponse('Account has been created successfully')
        else:
            return HttpResponse('Passwords do not match')
    else:
        wishlistItemsTotal = wishlist_items_total(request)
        cartIconTotal = cart_icon_total(request)
        context = {'wishlistItemsTotal': wishlistItemsTotal, 'cartIconTotal': cartIconTotal}
        return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone_or_email = data['phoneOrEmail']
        password = data['password']
        try:
            username = Customer.objects.get(phone_or_email=phone_or_email).user.username
        except:
            return JsonResponse({'errorMsg': 'No account with the given number exists'})

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse(f'{username} logged in')
        else:
            return JsonResponse({'errorMsg': 'Phone number/email or password is incorrect'})

    else:
        wishlistItemsTotal = wishlist_items_total(request)
        cartIconTotal = cart_icon_total(request)
        context = {'wishlistItemsTotal': wishlistItemsTotal, 'cartIconTotal': cartIconTotal}
        return render(request, 'accounts/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
