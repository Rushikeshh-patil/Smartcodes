from django.shortcuts import render
from django.http import HttpResponse #Each django request creates HttpRequest which is passed to the views. and a view must return a HttpResponse

def mechanical(request):
    
    return render(request, 'Mechanical_Codes/mechanical.html',{'title':'Mechanical Code'})
# Create your views here.

def about(request):
    
    return render(request, 'Mechanical_Codes/about.html',{'title':'About Smartcodes'})