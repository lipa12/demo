from django.db import models


# Create your models here.


class Register(models.Model):
     emailid=models.CharField(max_length=50)
     password=models.CharField(max_length=50)
     mobile=models.CharField(max_length=50)
     fullname=models.CharField(max_length=50)
     createdate=models.DateTimeField(auto_now=True)

     def __str__(self):
          return "Email id is " + self.emailid + "Password" + self.password + "Mobile no is" + self.mobile + "fullname is" + self.fullname + "Date is" + str(self.createdate)


class Review(models.Model):
      register=models.ForeignKey(Register,on_delete=models.CASCADE)
      rating=models.IntegerField()
      reviewto=models.CharField(max_length=50)
      reviewdesc=models.CharField(max_length=50)
      reviewdate=models.DateTimeField()