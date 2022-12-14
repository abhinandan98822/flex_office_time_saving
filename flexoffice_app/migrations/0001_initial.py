# Generated by Django 4.1 on 2022-08-22 10:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(blank=True, choices=[('', 'Select Any'), ('h', 'Half Day'), ('f', 'Full Day'), ('s', 'Short Leave')], default='f', max_length=2, null=True)),
                ('leave_status', models.CharField(blank=True, choices=[('', 'Select Any'), ('p', 'Paid Leave'), ('u', 'Unpaid Leave')], default='u', max_length=2, null=True)),
                ('status', models.CharField(choices=[('A', 'Absent'), ('P', 'Present'), ('L', 'Leave'), ('H', 'Holiday')], default='A', max_length=1)),
                ('note', models.TextField(blank=True, null=True)),
                ('check_in', models.DateTimeField(blank=True, null=True)),
                ('check_out', models.DateTimeField(blank=True, null=True)),
                ('attendance_date', models.DateField(default=datetime.datetime.now)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('month', models.IntegerField(default=8)),
                ('attended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Created_by', to=settings.AUTH_USER_MODEL)),
                ('employe_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BidDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractURL', models.CharField(max_length=100)),
                ('jobtitle', models.CharField(max_length=200)),
                ('jobdescription', models.TextField()),
                ('clientcountry', models.CharField(max_length=20)),
                ('Proposal', models.TextField()),
                ('connectsused', models.IntegerField()),
                ('projecttype', models.CharField(choices=[('F', 'Fixed'), ('H', 'Hourly')], max_length=2)),
                ('priceofproject', models.IntegerField()),
                ('clientreplied', models.CharField(max_length=200)),
                ('Comments', models.CharField(max_length=200)),
                ('Converted', models.CharField(max_length=100)),
                ('BidBy', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_leave_day', models.CharField(max_length=2)),
                ('paid_leave_day', models.CharField(max_length=2)),
                ('unpaid_leave_day', models.CharField(max_length=2)),
                ('bonus_amount', models.IntegerField(default=0)),
                ('paid_leave_amount', models.CharField(max_length=2)),
                ('unpaid_leave_amount', models.CharField(max_length=2)),
                ('paid_salary', models.CharField(max_length=20000)),
                ('deducted_salary', models.CharField(max_length=100)),
                ('half_leave', models.CharField(default=0, max_length=20)),
                ('month', models.IntegerField(default=7)),
                ('year', models.IntegerField(default=2022)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
                ('employeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flexoffice_app.salary')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryBonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('note', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('employee_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('tasks', models.TextField()),
                ('status', models.CharField(choices=[('morning', 'MORNING'), ('evening', 'EVENING')], default='morning', max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField(default=datetime.datetime.now, unique=True)),
                ('is_holiday', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_opened', models.ManyToManyField(blank=True, to='flexoffice_app.attendance')),
            ],
        ),
    ]
