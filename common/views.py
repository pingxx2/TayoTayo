from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
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
def myreserve(request):
    """
    나의 예약현황 출력
    """
    # 선택한 주차장 예약 리스트
    res = Res.objects.filter(user_id=request.user)

    context={
        'res':res,
    }

    return render(request, 'common/myreserve.html', context)

@login_required(login_url='common:login')
def myreserve_delete(request, res_id):
    """
    나의 예약현황에서 선택 행 삭제
    """
    delete_res = get_object_or_404(Res, pk=res_id)
    delete_res.delete()

    return redirect('/common/myreserve')

@login_required(login_url='common:login')
def parking_add(request):
    """
    parking 테이블에 값 추가
    """
    if request.method == 'POST':
        form = ParkingCreateForm(request.POST)
        if form.is_valid():
            parking = form.save(commit=False)
            parking.owner = request.user
            parking.save()

            return redirect('common:mypage')
    else:
        form = ParkingCreateForm()

    
    context={
        'form':form,
    }

    return render(request, 'common/add.html', context)

@login_required(login_url='common:login')
def mypage_detail(request, parking_number):
    """
    주차장 관리 출력
    """
    # 선택한 주차장 리스트
    parking_user = get_object_or_404(Parking, pk=parking_number)
    # 선택한 주차장 예약 리스트
    parking_res = Res.objects.filter(parking_number=parking_number)
    
    context = { 'parking_user' : parking_user, 'parking_res' : parking_res }

    return render(request, 'common/mypage_detail.html', context)


@login_required(login_url='common:login')
def parking_modify(request, parking_number):
    """
    parking 테이블 값 수정
    """
    parking_on = Parking.objects.get(parking_number=parking_number)

    if parking_on.res_state == "ON":
        parking_on.res_state = "OFF"
        parking_on.save()
    else:
        parking_on.res_state = "ON"
        parking_on.save()

    return redirect(f'/common/mypage/{parking_number}')



