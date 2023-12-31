# Generated by Django 4.2.7 on 2023-12-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=10, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]
