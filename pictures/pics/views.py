from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.

def landing(request):
  
    
    return render(request,'index.html')
def search(request):
  
    
    return render(request,'search.html')

def places(request):
  
    
    return render(request,'locs.html')


def naivasha(request):
  
    
    return render(request,'vasha.html')
    
def kisumu(request):
  
    
    return render(request,'sumu.html')
def nyeri(request):
  
    
    return render(request,'nyer.html')
def kitale(request):
  
    
    return render(request,'kit.html')
def nairobi(request):
  
    
    return render(request,'nai.html')
def watamu(request):
  
    
    return render(request,'wat.html')
