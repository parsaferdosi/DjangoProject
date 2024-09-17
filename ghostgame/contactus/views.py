from django.shortcuts import render,redirect
from .forms import ticketform
from .models import ticket
def ticketmanager(request):
    if request.method=="POST":
        form=ticketform(request.POST)
        if form.is_valid():
            ticket.objects.create(
            firstname = form.cleaned_data['name'],
            lastname = form.cleaned_data['surname'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            
            )
            return redirect("homescreen:welcom-page")
    else:
        form=ticketform()
    return render(request ,'contactus/contact.html',{'form':form})
