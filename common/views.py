from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404, redirect
from common.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Parking
from .forms import ParkingCreateForm

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            phone_number = form.cleaned_data.get('phone_number')
            user = authenticate(password=raw_password, phone_number=phone_number)
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'common/signup.html', {'form': form})


def mypage(request):
    return render(request, 'common/mypage.html')

def add(request):
    return render(request, 'common/add.html')


@login_required(login_url='common:login')
def parking_add(request):
    """
    parking 테이블에 값 추가
    """
    if request.method == 'POST':
        form = ParkingCreateForm(request.POST)
        if form.is_valid():
            parking = form.save(commit=False)
            messages(Warning, parking.lat())
            messages(Warning, parking.lon())
            parking.owner = request.user
            parking.save()

            return redirect('common:mypage')
    else:
        form = ParkingCreateForm()
    
    context={'form':form}

    return render(request, 'common/add.html', context)
