from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image
# Create your views here.

def landing(request):
    pics = Image.all_pics()
    return render(request,'index.html',{"pics": pics})

def search(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
    return render(request, 'search.html', {'message':message})


def places(request):
  
    
    return render(request,'locs.html')


def naivasha(request):
    catt = 'naivasha' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'vasha.html',{"pics":pics})
    
def kisumu(request):
    catt = 'kisumu' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'sumu.html',{"pics":pics})
def nyeri(request):
    catt = 'nyeri' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'nyer.html',{"pics":pics})
def kitale(request):
    catt = 'kitale' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'kit.html',{"pics":pics})
def nairobi(request):
    catt = 'nairobi' 
    pics = Image.objects.filter(location__locname=catt).all()
    
    return render(request,'nai.html',{"pics":pics})
def watamu(request):
    catt = 'watamu' 
    pics = Image.objects.filter(location__locname=catt).all() 
    
    return render(request,'wat.html',{"pics":pics})
