from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def LoginFn(request):
    if request.method=="POST":
        username=request.POST['usr_name']
        Password=request.POST['pass']
        students=Student_details.objects.get(user_name=username)
        try:
            if username==students.user_name and Password==students.Password and students.user_type==False:
                request.session['loggedUser']=students.id 
                return redirect('student_home')
            elif username==students.user_name and Password==students.Password and students.user_type==True: 
                 return redirect('dashbord')
            else:
                return render(request,'login_form.html')
        except students.DoesNotExist:
            return render( request,'login_form.html',{'message':'login failed'})      
    return render(request,'login_form.html')

def registerFn(request):
    if request.method=="POST":
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['mail']
        username=request.POST['uname']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        student=Student_details(name=name,contact=contact,Email=email,user_name=username,Password=password,Conf_password=confirm_password,)
        student.save()

    return render(request,'student_registration.html')
def dashbordFn(request):
    return render(request,'admin_dashbord.html')

def student_dashbordFn(request):
    return render(request,'student_dashbord.html')

def detailsFn(request):
    currentSession=request.session['loggedUser']
    students=Student_details.objects.filter(id=currentSession)
    return render(request,'student_details.html',{'details':students})

def editFn(request,id):
    edit_data=Student_details.objects.get(id=id)
    if edit_data.status==True:
        return render(request,'student_updation.html',{'edit':edit_data})
    else:
        return redirect('student_details')



    # return render(request,'student_updation.html',{'edit':edit_data})
def updateFn(request,id):
    if request.method=="POST":
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['mail']
        username=request.POST['uname']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        Student_details.objects.filter(id=id).update(name=name,contact=contact,Email=email,user_name=username,Password=password,Conf_password=confirm_password,)
    return redirect('student_details')

def activeFn(request):
    active_students=Student_details.objects.filter(status=True)        
    return render(request,'active.html',{'active':active_students})

def inactiveFn(request):
    inActive_students=Student_details.objects.filter(status=False)        
    return render(request,'inactive.html',{'inActive':inActive_students})
def inactivateFn(request,id):
    Student_details.objects.filter(id=id).update(status=False)
    return redirect('active')
def activateFn(request,id):
    Student_details.objects.filter(id=id).update(status=True)
    return redirect('inactive')




    
