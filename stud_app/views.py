from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def our_department(request):
    return render(request, 'our_department.html')

def dashboard(request):
    return render(request, 'admin dashboard/dashboard.html')

def year_log(request):
     return render(request, 'admin dashboard/year_log.html')
 
def stud_mgt(request):
    return render(request, 'admin dashboard/stud_mgt.html')

def Login(request):
    return render(request, 'login.html')

def Register(request):
    return render(request, 'register.html')

