from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required
from .models import Department,Year,Student
from .forms import DepartmentForms,YearForms,StudentForms


def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def our_department(request):
    return render(request, 'our_department.html')

@login_required(login_url='login')
def dashboard(request):
    dpt_details = Department.objects.all()

    context = {
        'dpt_details':dpt_details
    }
    return render(request, 'admin dashboard/dashboard.html',context)

def year_log(request):
     return render(request, 'admin dashboard/year_log.html')
 
def stud_mgt(request):
    return render(request, 'admin dashboard/stud_mgt.html')

def add_department(request,pk=None):
    instance = None
    if pk:
        instance = get_object_or_404(Department,pk=pk)

    if request.method == 'POST':
        form = DepartmentForms(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()

            return redirect('dashboard')
    else:
        form = DepartmentForms(instance=instance)

    context = {
        'form':form,
    }    
        
    return render(request, 'admin dashboard/add_department.html',context)

def delete_department(request, pk = None):
    del_dpt = get_object_or_404(Department,pk = pk)
    del_dpt.delete()
    return redirect('dashboard')


def add_student(request,pk = None):
    instance = None
    if pk:
        instance = get_object_or_404(Student,pk=pk)

    if request.method == 'POST':
        form = StudentForms(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()

            return redirect('stud_mgt')
    else:
        form = StudentForms(instance=instance)

    context = {
        'form':form,
    }

    return render(request, 'admin dashboard/add_student.html',context)

def delete_student(request, pk = None):
    del_stud = get_object_or_404(Student,pk = pk)
    del_stud.delete()
    return redirect('stud_mgt')



def add_year_form(request,pk = None):
    instance = None
    if pk:
        instance = get_object_or_404(Year,pk=pk)

    if request.method == 'POST':
        form = YearForms(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()

            return redirect('year_log')
    else:
        form = YearForms(instance=instance)

    context = {
        'form':form,
    }

    return render(request, 'admin dashboard/add_year_form.html',context)

def delete_Year(request, pk = None):
    del_year = get_object_or_404(Year,pk = pk)
    del_year.delete()
    return redirect('year_log')


def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
           
            login(request, user)
            return redirect('login')  
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('homepage')

