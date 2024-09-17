from django.shortcuts import render , redirect
from .forms import userRegisterForm,userLoginForm,ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
def ViewLogin(request):
    if request.method == 'POST':
        form_login = userLoginForm(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(request, username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect("home:welcmoe-page")
            else:
                print("Authentication failed")
        else:
            print("Form is not valid")
    else:
        form_login = userLoginForm()

    context = {'form_login': form_login}
    return render(request, 'contact/login.html', context)
def ViewContactUs(request):
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
            return redirect("home:welcmoe-page")
    else:
        form_register=userRegisterForm
    context={'form_register':form_register}
    return render(request,'contact/contactpage.html',context)


def viewLogout(request):
    logout(request)
    return redirect("home:welcmoe-page")
@login_required
def viewChangePassword(request):
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        user=request.user
        if form.is_valid():
            data=form.cleaned_data
            old_pass=data['old_pass']
            new_password1=data['new_pass1']
            new_password2=data['new_pass2']
            if not user.check_password(old_pass):
                return HttpResponse("پسورد اشتباه است")
            elif new_password1 != new_password2:
                return HttpResponse('not match')
            else:
                user.set_password(new_password1)
                login(request,user)
                user.save()
                return redirect('home:welcom-page')
    else:
        form=ChangePasswordForm
    return render(request,'contact/changepassword.html',{'form':form})