from django.shortcuts import redirect, render
from Crud.models import Employees


def INDEX(request):

    emp = Employees.objects.all()

    context = {
        'emp':emp
    }

    return render(request, 'crud.html', context)


def Add(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')


        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'crud.html')


def Edit(request):
    emp = Employees.objects.all()

    context ={
        "emp":emp, 
    }
    return render(request, 'crud.html', context )



def Update (request, id):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone') 

        emp = Employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'crud.html' )



def Delete (request, id):
    
    emp = Employees.objects.filter(id= id)
    emp.delete()
    
    context = {
        'emp' : emp,
    }
    return redirect('home')