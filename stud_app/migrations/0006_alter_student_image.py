# Generated by Django 4.2.7 on 2023-12-12 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0005_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='stud_app/images'),
        ),
    ]