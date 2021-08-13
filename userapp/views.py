from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from .models import Register,Review
from reviewadmin.models import CompanyMaster
from django.utils import timezone

print(make_password('1234'))
print(check_password('1234','pbkdf2_sha256$260000$p37duBvrflRG0XLOV54DD6$VaJYcBA/thV1ic5x1DXAgyh8aS3whwPjgdTJq2Sg7P8='))

# Create your views here.

def home(request):
    if request.method=="POST":
        s=Register.objects.filter(emailid=request.POST["txtemail"]).values_list('id','password')
        pass1=s[0][1]
        if s.count()>0 and check_password(request.POST["txtpass"],pass1):
            print("ID is ",s[0][0])

            request.session["rid"]=s[0][0]
            return redirect('dashboard')
        else:
            return render(request,"userapp/home.html",{"msg":"invalid userid and password"})
    return render(request,"userapp/home.html")

def dashboard(request):
    if request.session.has_key("rid"):
        data=Register.objects.get(pk=request.session["rid"])
        return render(request,"userapp/dashboard.html",{'res':data})
    else:
        return redirect("/")

def about(request):
    return render(request,"userapp/about.html")

def account(request):
    if request.method=="POST":
        obj=Register(emailid=request.POST["txtemail"],password=make_password(request.POST["txtpass"]),mobile=request.POST["txtmobile"],fullname=request.POST["txtfname"],createdate=timezone.now())
        obj.save()
        return render(request,"userapp/account.html",{"msg":"Registration Successfully"})
    return render(request,"userapp/account.html")
def editprofile(request):
    if request.method=="POST":
        obj=Register.objects.get(pk=request.session["rid"])
        obj.emailid=request.POST["txtemail"]
        obj.password=request.POST["txtpass"]
        obj.mobile=request.POST["txtmobile"]
        obj.fullname=request.POST["txtfname"]
        obj.createdate=obj.createdate
        obj.save()
        return redirect('dashboard')
    obj=Register.objects.get(pk=request.session["rid"])
    return render(request,"userapp/editprofile.html",{'res':obj})


def managereview(request):
    stars={'5':'*****','4':'****','3':'***','2':'**','1':'*'}
    company=CompanyMaster.objects.all
    if request.method=="POST":
      if(Review.objects.filter(register_id=request.session["rid"],reviewto=request.POST["txtreviewto"]).count()==0):
        rto=request.POST["txtother"] if request.POST["txtreviewto"]=="other" else request.POST["txtreviewto"]
        obj=Review(register_id=request.session["rid"],rating=request.POST["txtrating"],reviewto=rto,reviewdesc=request.POST["txtdesc"],reviewdate=timezone.now())
        obj.save()
        return redirect('/managereview')
      else:
          r=Review.objects.filter(register_id=request.session["rid"],reviewto=request.POST["txtreviewto"]).values_list('id')
          return redirect('/editreview?q='+str(r[0][0]))
        #return render(request,"userapp/managereview.html",{"reviewdata":Review.objects.filter(register_id=request.session["rid"]),"msg":"You have already provided review to this company",'star':stars})

    return render(request,"userapp/managereview.html",{"reviewdata":Review.objects.filter(register_id=request.session["rid"]),'star':stars,'com':company})


def editreview(request):
    stars={'5':'*****','4':'****','3':'***','2':'**','1':'*'}
    if request.method=="POST":
        r=Review.objects.get(pk=request.POST["txtid"])
        res=Review.objects.filter(register_id=request.session["rid"],reviewto=request.POST["txtreviewto"]).exclude(id=request.POST["txtid"])

        if res.count()==0:
            r=Review.objects.get(pk=request.POST["txtid"])
            r.register_id=request.session['rid']
            r.rating=request.POST['txtrating']
            r.reviewto=request.POST['txtreviewto']
            r.reviewdesc=request.POST['txtdesc']
            r.reviewdate=timezone.now()
            r.save()
            return redirect('/managereview')
        else:
            return HttpResponse("<script>alert('Review Already Assigneded to that company');window.location='/managereview';</script>")



    else:
        res=Review.objects.get(pk=request.GET["q"])
        return render(request,"userapp/editreview.html",{"data":res,'star':stars})

def deletereview(request):
    r=Review.objects.get(pk=request.GET["q"])
    r.delete()
    return redirect('/managereview')

def logout(request):
    del request.session['rid']
    return redirect('/')


