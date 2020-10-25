from os import name
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Province, Cafe
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(req):
    cafe = Cafe.objects.all().order_by('?')[:6] # สุ่มมา 6 อัน
    context = {
        'cafes': cafe
    }
    return render(req, template_name='myweb/index.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'myweb/signup.html', {'form': form})


def addContact(req):
    fullname = req.POST.get('name')
    email = req.POST.get('email')
    desc = req.POST.get('desc')
    contact = Contact(fullname=fullname, email=email, desc=desc)
    contact.save()
    return redirect('index')


def cafeinfo(req, id):
    cafe = Cafe.objects.get(id=id)
    return render(req, 'myweb/cafeinfo.html', context={'cafe':cafe})

@login_required
def search(req):
    province = Province.objects.all().order_by('name')
    if req.method == "POST":
        keyword = req.POST.get('province')
        cafes = Cafe.objects.filter(province__name=keyword)
        return render(req, 'myweb/search.html', {'provinces':province, 'cafes':cafes})
    else:
        return render(req, 'myweb/search.html', {'provinces':province})