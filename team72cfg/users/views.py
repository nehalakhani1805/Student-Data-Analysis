from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
# Create your views here.'

def home(request):
    return render(request,'users/home.html')
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})
def profile(request):
    if request.method=='POST':
        uform=UserUpdateForm(request.POST, instance=request.user)
        pform=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        uform=UserUpdateForm(instance=request.user)
        pform=ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html',{'uform':uform,'pform':pform})