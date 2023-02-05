from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404, redirect
from common.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Parking, Res
from .forms import ParkingCreateForm
import json

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

    parkings = Parking.objects.all()
    
    context={
        'form':form,
        'parkings_js' : json.dumps([pkg.json() for pkg in parkings]),
    }

    return render(request, 'common/add.html', context)

@login_required(login_url='common:login')
def parking_modify(request, parking_number):
    """
    parking 테이블 값 수정
    """
    parking = get_object_or_404(Parking, pk=parking_number)
    if request.user != parking.owner:
        messages.error(request, "변경권한이 없습니다.")
        return redirect('common:mypage_detail')
    if request.method == "POST":
        form = ParkingCreateForm(request.POST, instance=parking)
        if form.is_valid():
            parking = form.save(commit=False)
            if(parking.res_state=="ON"):
                parking.res_state="OFF"
            else:
                parking.res_state="ON"
            parking.save()
            return redirect('common:mypage_detail')
    else:
        form = ParkingCreateForm(instance=parking)
    
    context={
        'form' : form
    }

    return render(request, 'common/mypage_detail.html', context)

@login_required(login_url='common:login')
def mypage_detail(request, parking_number):
    """
    주차장 관리 출력
    """
    parking_user = get_object_or_404(Parking, pk=parking_number)
    context = { 'parking_user' : parking_user }

    return render(request, 'common/mypage_detail.html', context)
