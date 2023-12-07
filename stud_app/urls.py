from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='homepage'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('our_department/',views.our_department,name='our_department'),
    path('year_log/',views.year_log,name='year_log'),
    path('stud_mgt/',views.stud_mgt,name='stud_mgt'),

    path('dashboard/',views.dashboard,name='dashboard'),

    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),
    path('logout/',views.Logout,name='logout'),
    path('add_department/',views.add_department,name = 'add_department'),
    path('add_student/',views.add_student,name = 'add_student'),
    path('add_year_form/',views.add_year_form,name = 'add_year_form')



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
