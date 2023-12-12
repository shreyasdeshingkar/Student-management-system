from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required
from .models import Department,Year,Student,Contact
from .forms import DepartmentForms,YearForms,StudentForms,ContactForms


def home(request):
    return render(request, 'index.html')

def contact(request):
    
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForms()

    context = {
        'form' : form 
    }

    return render(request, 'contact.html',context)

def delete_contact(request,pk = None):
    contact_del_details = get_object_or_404(Contact,pk = pk)
    contact_del_details.delete()
    return redirect('contact_log')




def about(request):
    return render(request, 'about.html')


def our_department(request):
    year_details = Year.objects.all()

    context = {
        'year_details' : year_details
    }
    return render(request, 'our_department.html',context)

@login_required(login_url='login')
def dashboard(request):
    dpt_details = Department.objects.all()

    context = {
        'dpt_details':dpt_details
    }
    return render(request, 'admin dashboard/dashboard.html',context)

def year_log(request):
    year_details = Year.objects.all()

    context = {
        'year_details':year_details
    }

    return render(request, 'admin dashboard/year_log.html',context)
 
def stud_mgt(request):
    student_details = Student.objects.all()

    context = {
        'student_details':student_details
    }
    return render(request, 'admin dashboard/stud_mgt.html',context)

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



def contact_log(request):
    contact_details = Contact.objects.all()

    context = {
        'contact_details':contact_details
    }
    return render(request, 'admin dashboard/contact_log.html',context)



def our_students(request,pk = None):
    year_details = Year.objects.get(pk = pk)
    students = Student.objects.filter(year = year_details)

    context = {
        'year_details':year_details,
        'students':students
    }
    return render(request, 'our_students.html',context)

def students_profile(request,pk = None):
    student_details = get_object_or_404(Student,pk = pk)

    context = {
        'student':student_details,

    }
    return render(request, 'students_profile.html',context)




