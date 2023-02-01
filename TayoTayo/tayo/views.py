from django.shortcuts import render

def main(request):
    return render(request, 'tayo/main.html')

def reserve(request):
    return render(request, 'tayo/reserve.html')

def info(request):
    return render(request, 'tayo/info.html')

def parking(request):
    return render(request, 'tayo/parking.html')
