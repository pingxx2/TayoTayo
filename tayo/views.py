from django.shortcuts import render, redirect, get_object_or_404
from common.models import Parking, Res
from django.contrib.auth.decorators import login_required
from .forms import ResForm
from datetime import datetime, timedelta

def main(request):
    return render(request, 'tayo/main.html')

def reserve(request):
    """
    예약하기
    """
    # 전체 주차장 리스트 불러오기
    parking_list = Parking.objects.all()

    # context에 담아서 tayo/reserve.html에 전송
    context ={
        'parking_list' : parking_list
    }
    return render(request, 'tayo/reserve.html', context)

@login_required(login_url='common:login')
def reserve_add(request):
    """
    예약 추가
    """
    if request.method == 'POST':
        form = ResForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            res.end_time = (datetime.now() + timedelta(hours=int(request.POST['time']))).strftime("%Y-%m-%d %H:%M:%S")
            res.user_id = request.user
            res.save()

            return redirect('common:myreserve')
    else:
        form = ResForm()

    
    context={
        'form':form,
    }

    return render(request, 'common/myreserve.html', context)


def info(request):
    return render(request, 'tayo/info.html')

def parking(request):
    # 전체 주차장 리스트 불러오기
    parking_list = Parking.objects.all()

    # context에 담아서 tayo/reserve.html에 전송
    context ={
        'parking_list' : parking_list
    }
    return render(request, 'tayo/parking.html', context)