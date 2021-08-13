from django.db import models

# Create your models here.

class Regadmin(models.Model):
    emailid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    createdate=models.DateTimeField()
    def __str__(self):
        return "Email id is "+self.emailid+" password "+self.password+" Date is "+ str(self.createdate)

class CompanyMaster(models.Model):
    companyname=models.CharField(max_length=50)
    def __str__(self):
        return "Company name is "+self.companyname
