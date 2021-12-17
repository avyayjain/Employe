from django.shortcuts import render,redirect
from .models import Employee
from .forms import Employee_form

def addForm(request,id = 0):
    if request.method == 'GET':
        if id == 0:
            form = Employee_form()
        else:
            
            employee = Employee.objects.get(pk = id)
            form = Employee_form(instance=employee)

        return render(request,'add_form.html',{'form':form})

    else:
        if id == 0:
            form = Employee_form(request.POST,request.FILES)
        else:
            employee = Employee.objects.get(pk = id)
            form = Employee_form(request.POST,request.FILES,instance=employee)
        if form.is_valid():

            form.save()
        return redirect('data')

def showForm(request):
    employee = Employee.objects.all()
    return render(request,'showcarddata.html',{'employee':employee})

def deleteForm(request,id):
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('data')








# Create your views here.
# from django.http import HttpResponse

"""def hello(request):
    return HttpResponse('hello world')

def add(request):
    if request.method == 'POST':
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        c = a+b
        name = 'Avyay jain'
        context = {
            'result':c,
            'name': name,                
        }
        return render(request,'add.html',context)
    
    else: 
        return render(request,'add.html')"""






