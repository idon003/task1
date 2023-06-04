# Generated by Django 4.2 on 2023-06-04 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('emergency_contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('marital_status', models.CharField(blank=True, max_length=20, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('work_location', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_joining', models.DateField(auto_now_add=True)),
                ('reporting_to', models.CharField(blank=True, max_length=50, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='employee/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField(auto_now_add=True)),
                ('nature_of_leave', models.CharField(max_length=50)),
                ('first_day', models.DateField()),
                ('last_day', models.DateField()),
                ('number_of_days', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]