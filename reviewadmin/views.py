from django.shortcuts import render,redirect
from .models import Regadmin,CompanyMaster

# Create your views here.

def home(request):
    if request.method=="POST":
        print("hello")
        res=Regadmin.objects.filter(emailid=request.POST["txtemail"],password=request.POST["txtpass"])
        if res.count()>0:
            return redirect('/reviewadmin/dashboard')
        else:
            return render(request,"reviewadmin/home.html",{"msg":"Invalid userid and password"})
    return render(request,"reviewadmin/home.html")

def dashboard(request):
    if request.method=="POST":
        obj= CompanyMaster(companyname=request.POST["txtcompany"])
        obj.save()
        return render(request,"reviewadmin/dashboard.html",{"msg":'company added'})
    return render(request,"reviewadmin/dashboard.html")
