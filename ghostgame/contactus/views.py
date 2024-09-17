from django.shortcuts import render

def viewContactUs(request):
    return render(request,'contactus/contact.html')