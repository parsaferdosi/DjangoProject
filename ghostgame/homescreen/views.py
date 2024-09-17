from django.shortcuts import render
from django.views.generic import ListView
from .models import suggestion,gamegenre
from django.shortcuts import get_object_or_404
def viewhome(request):
    obj=suggestion.objects.all()
    return render(request,'homescreen/index.html',{'a':obj})
def gamelist(request):
    ogj=suggestion.objects.all()
    obj=gamegenre.objects.all()
    return render(request,'homescreen/shop.html',{'games':ogj,'tag':obj})
def moresiscription(request,m):
    obj=get_object_or_404(suggestion,slug=m)
    return render(request,"homescreen/product-details.html",{'obj':obj})
def search_future(request):
    if request.method=="POST":
        search_query=request.POST["searchKeyword"]
        posts=suggestion.objects.filter(gamename=search_query)
        return render(request,'homescreen/shop.html',{'tag':search_query,'a':posts})