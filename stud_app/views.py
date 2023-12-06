from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'admin dashboard/dashboard.html')

def year_log(request):
     return render(request, 'admin dashboard/year_log.html')
 
def stud_mgt(request):
    return render(request, 'admin dashboard/stud_mgt.html')




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

