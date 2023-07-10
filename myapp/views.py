
from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    
  
    
    # isactive=True
    
    # age=19
    
    # data={
    #     'isactive':isactive,
    #     'value':value,
    #     'age':age
    # }
    
    return render(request,"home.html",{});
    



def about(request):
    return render(request,"about.html",{});
    


def services(request):
    return HttpResponse("<h1> This is the services page </h1>");
