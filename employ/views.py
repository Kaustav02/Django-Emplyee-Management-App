from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import emp 


# Create your views here.

def emp_home(request):
    emps = emp.objects.all()
    return render(request,'emp/home.html',{'emps':emps})


def add_emp(request):
    if request.method=="POST":
        
        # fetching data from request
        
        emp_name = request.POST.get("emp_name");
        emp_id = request.POST.get("emp_id");
        emp_phone = request.POST.get("emp_phone");
        emp_adress = request.POST.get("emp_adress");
        emp_working = request.POST.get("emp_working");
        emp_depertment = request.POST.get("emp_depertment");
        
         
        e=emp()
        
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.adress=emp_adress
        
        e.depertment=emp_depertment
        
        if emp_working is None:
            e.working=False
        else:
            e.working=True    
        
        ## saving the object
        
        e.save()
        
        
        
        
        
        return redirect("/emp/home/")
    return render(request,'emp/add_emp.html',{})


    
def delete_emp(request,emp_id):
    Emp = emp.objects.get(pk=emp_id)
    Emp.delete()
    
    return redirect("/emp/home/")


def update_emp(request , emp_id):
    Emp = emp.objects.get(pk=emp_id)
    
    return render(request,"emp/update_emp.html",{
        'emp':Emp
    })
    
def do_update(request):
    
    if request.method == 'POST':
        emp_name = request.POST.get("emp_name");
        emp_id = request.POST.get("emp_id");
        emp_phone = request.POST.get("emp_phone");
        emp_adress = request.POST.get("emp_adress");
        emp_working = request.POST.get("emp_working");
        emp_depertment = request.POST.get("emp_depertment");
    
    
        
    return redirect("/emp/home")


