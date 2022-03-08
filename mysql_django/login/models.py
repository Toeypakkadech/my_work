from django.db import models
from django import forms

class Employee(models.Model):
    fistname =models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    gender =models.CharField(max_length=50,choices=[('ชาย','ชาย'),('หญิง','หญิง')],default='ชาย')
    position =models.CharField(max_length=30)
    salary = models.PositiveIntegerField()
    address = models.TextField(max_length=200)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=30, unique=True)
    birthday = models.DateField()
    religion = models.CharField(max_length=20, choices=[('พุทธ','พุทธ'), ('ศริสต์','ศริสต์'), ('อิสลาม','อิสลาม'), ('อื่นๆ','อื่นๆ')],default='พุทธ')
    addition_note = models.TextField(null=True, blank=True)


   

class Employeeforms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        label = {
            'fistname' : 'ชื่อ',
            'lastname' : 'นามสกุล',
            'gender' : 'เพศ',
            'position' : 'ตำแหน่งงาน',
            'salary' : 'เงินเดือน',
            'address' : 'ที่อยู่',
            'email' : 'อีเมล',
            'phone' : 'โทรศัพท์',
            'birthday' : 'วันเกิด',
            'religion' : 'ศาสนา',
            'addition_note' : 'บันทึกเพิ่มเติม',
        }
        widgets = {
            'gender' : forms.RadioSelect(),
            'birthday' : forms.DateInput(attrs={'type': 'data'}),
            'religion' : forms.Select(),
            'address' : forms.Textarea(attrs={'row':'3'}),
            'addition_note' : forms.Textarea(attrs={'row':'3'})
        }

class Member(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class Memberform(forms.ModelForm):
    confirm_pswd = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )
    save = forms.BooleanField(required=False)

    class Meta:
        model = Member
        fields = '__all__'
        Widgets = {
            'password' : forms.PasswordInput()
        }