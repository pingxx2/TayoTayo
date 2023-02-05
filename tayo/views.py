from django.shortcuts import render
from django.contrib.auth.models import User
from common.models import Parking, Res

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

def info(request):
    return render(request, 'tayo/info.html')

def parking(request):
    return render(request, 'tayo/parking.html')
