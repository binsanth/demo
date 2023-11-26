from django.http import HttpResponse
from django.shortcuts import render
from . models import travel_table
from . models import team

def demo(request):
    obj=travel_table.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'obj':obj,'obj1':obj1})
