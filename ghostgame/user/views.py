from django.shortcuts import render,redirect
from .forms import userRegisterForm,userLoginForm,ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def profileView(request):
    return render(request,'user/profile.html')
def ViewLogin(request):
    if request.method == 'POST':
        form_login = userLoginForm(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect("homescreen:welcom-page")
            else:
                print("Authentication failed")
        else:
            print("Form is not valid")
    else:
        form_login = userLoginForm()
    form = {'form_login': form_login}
    return render(request, 'user/login.html', form)
def registerView(request):
    if request.method=="POST":
        form_register=userRegisterForm(request.POST)
        if form_register.is_valid():
            data=form_register.cleaned_data
            User.objects.create_user(
                username=data['user_name'],
                email=data['email'],
                first_name=data['firstname'],
                last_name=data['lastname'],
                password=data['password2']
            )
            return redirect("homescreen:welcom-page")
    else:
        form_register=userRegisterForm
    form={'form_register':form_register}
    return render(request,'user/register.html',form)