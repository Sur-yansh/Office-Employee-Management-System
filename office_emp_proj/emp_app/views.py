from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps= Employee.objects.all()
    context={
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method=='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        salary= request.POST['salary']
        role= request.POST['role']
        dept= request.POST['dept']
        bonus= request.POST['bonus']
        phone= request.POST['phone']
        hire_date= request.POST['hire_date']
        new_emp= Employee(first_name= first_name, last_name= last_name, salary= salary, role_id= role, bonus=bonus, phone=phone, dept_id=dept, hire_date=datetime.now())
        new_emp.save
        return HttpResponse('Employee Added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception Error')

def remove_emp(request, emp_id = 0 ):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID") 
            
    emps= Employee.objects.all()
    
    context = {
        'emps' : emps
    }
    return render(request, 'remove_emp.html', context)

  
def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        role = request.POST['role']
        dept = request.POST['dept']
        emps= Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if role:
            emps = emps.filter(role__name__icontains = role)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
            
        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)
        
    elif request.method =="GET":
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
    