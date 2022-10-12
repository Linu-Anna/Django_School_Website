# from django.http import HttpResponse
from django.shortcuts import render
from .models import Department,Course
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404




def message(request):
    return render(request,'message.html')
def form(request):
    return render(request,'form.html')

def newpage(request):
    return render(request,'newpage.html')
def home(request):
    return render(request,'index.html')
#