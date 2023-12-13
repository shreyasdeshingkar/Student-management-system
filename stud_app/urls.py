from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='homepage'),
    path('contact/',views.contact,name='contact'),
    path('contact/delete/<int:pk>/',views.delete_contact,name='delete_contact'),
    path('about/',views.about,name='about'),
    path('our_department/',views.our_department,name='our_department'),
    path('year_log/',views.year_log,name='year_log'),
    path('stud_mgt/',views.stud_mgt,name='stud_mgt'),

    path('dashboard/',views.dashboard,name='dashboard'),

    path('login/',views.Login,name='login'),
    path('register/',views.Register,name='register'),
    path('logout/',views.Logout,name='logout'),
    path('add_department/',views.add_department,name = 'add_department'),
    path('add_department/<int:pk>/',views.add_department,name = 'update_department'),
    path('add_department/delete/<int:pk>/',views.delete_department,name = 'delete_department'),



    path('add_student/',views.add_student,name = 'add_student'),
    path('add_student/<int:pk>/',views.add_student,name = 'update_student'),
    path('add_student/delete/<int:pk>/',views.delete_student,name = 'delete_student'),


    path('add_year_form/',views.add_year_form,name = 'add_year_form'),
    path('add_year_form/<int:pk>/',views.add_year_form,name = 'update_year'),
    path('add_year_form/delete/<int:pk>/',views.delete_Year,name = 'delete_year'),




    path('our_students/<int:pk>/',views.our_students,name='our_students'),
    path('student/<int:pk>/',views.students_profile,name='students_profile'),
   



    path('contact_log/',views.contact_log,name='contact_log')






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
 

