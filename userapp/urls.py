from django.urls import path

from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('account',views.account, name='account'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('managereview',views.managereview,name='managereview'),
    path('editreview',views.editreview,name='editreview'),
    path('deletereview',views.deletereview,name='deletereview'),
]
