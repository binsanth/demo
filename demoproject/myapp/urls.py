from . import views
from django.urls import path

urlpatterns = [

    path('',views.newfun,),
    path('login',views.login,),
    path('logout',views.logout,),

]