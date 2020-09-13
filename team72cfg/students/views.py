from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegistrationForm
# Create your views here.
@login_required
def mystudents(request, id):
    if request.user.id==id:
        print(id)
        t=User.objects.filter(id=id).first()
        print(t)
        st=Student.objects.filter(teacher=t)
        print(st)
        return render(request, 'students/mystudents.html',{'st':st})
    else:
        return render(request, 'students/error.html')

@login_required
def register(request):
	context ={}

	form = StudentRegistrationForm(request.POST or None, request.FILES or None)
	
	if form.is_valid(): 
		form.save() 
		username=form.cleaned_data.get('firstname')
		messages.success(request,f'{username} registered !!')
		return redirect('home')
	context['form']= form 
	return render(request,'students/register.html',context) 

    



