from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
    
    
class Year(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name



GENDERCHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)
class Student(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=50,choices=GENDERCHOICES,null=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=10) 
    address = models.TextField(null=True)
    prn = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='stud_app/images',null=True)




class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=50, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    message = models.TextField(null=True)


     




