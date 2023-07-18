from django.shortcuts import render, redirect
from .models import empdata

def homepage(request):
    emp1=empdata.objects.all()
    return render(request,'addingmain.html', {'emp':emp1})



def addingmain(request):
    if request.method == 'GET':
        return render(request,'homepage.html')
    else:
        empdata(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        cname=request.POST['cname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        htown=request.POST['htown'],
        qualification=request.POST['qualification'],
        percentage=request.POST['percentage'],
        passoutyear=request.POST['passoutyear']
        ).save()
        return redirect(homepage)




def updata(request,id):
    emp=empdata.objects.get(id=id)
    return render(request,'updating.html',{'i':emp})



def updating_emp(request,id):
    emp=empdata.objects.get(id=id)
    emp.first_name=request.POST['fname']
    emp.last_name=request.POST['lname']
    emp.cname=request.POST['cname']
    emp.email=request.POST['email']
    emp.mobile=request.POST['mobile']
    emp.htown=request.POST['htown']
    emp.qualification=request.POST['qualification']
    emp.percentage=request.POST['percentage']
    emp.passoutyear=request.POST['passoutyear']
    emp.save()
    return redirect(homepage)





def delete_emp(request,id):
    emp=empdata.objects.get(id=id)
    emp.delete()
    return redirect(homepage)
