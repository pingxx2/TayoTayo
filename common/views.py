from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserCreationForm, UserChangeForm
from django.contrib import messages

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