from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from main.models import item


@login_required()
def homepage(request):
    count = item.objects.filter(owner=True).count()
    return render(request, 'main/index.html', context={'count': count})


@login_required()
def itempage(request):
    if request.method == 'GET':
        items = item.objects.filter(owner=None)
        count = item.objects.filter(owner=True).count()
        return render(request, 'main/items.html', context={'items': items, 'count': count})
    if request.method == 'POST':
        purchased_item = request.POST.get('purchased-item')
        print(purchased_item)
        if purchased_item:
            object = item.objects.get(name=purchased_item)
            object.owner = request.user
            object.save()
            messages.success(request,
                             f"Congratulations!!! the product {object.name} for {object.price} You have just bought!!!")
            return redirect('item')


def order(request):
    item_list = item.objects.filter(owner=True)
    count = item_list.count()
    return render(request, 'main/order.html', context={'item_list': item_list, 'count': count})


def orderCancel(request):
    if request.method == 'POST':
        purchased_item = request.POST.get('cancel-item')
        if purchased_item:
            object = item.objects.get(name=purchased_item)
            request.user = None
            object.owner = request.user
            object.save()
            messages.success(request,
                             f"Your order {object.name} Successfully Cancel!!!")
            return redirect('order')


def loginpage(request):
    if request.method == 'GET':
        return render(request, 'main/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'main/login.html')


def registerpage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password1 = form.cleaned_data.get('password2')
            if password == password1:
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('login')
        else:
            return redirect('register')
    return render(request, 'main/register.html')


def logoutpage(request):
    logout(request)
    return redirect('home')
