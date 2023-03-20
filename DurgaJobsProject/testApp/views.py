from django.shortcuts import render
from testApp.models import *
# Create your views here.
def home(request):
    return render(request, 'testApp/home.html')
def hydjobs1(request):
    jobs_list = hydjobs.objects.order_by('date')
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/hydjobs.html',context=my_dict)
def blorejobs(request):
    jobs_list = blorejobs.objects.order_by('date')
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/blorejobs.html',context=my_dict)

def chennaijobs(request):
    jobs_list = chennaijobs.objects.order_by('date')
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/chennaijobs.html',context=my_dict)

def punejobs(request):
    jobs_list = punejobs.objects.order_by('date')
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testApp/punejobs.html',context=my_dict)

