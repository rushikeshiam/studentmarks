from django.contrib import messages
from django.contrib.auth.backends import UserModel
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login 

from student.forms import AddStudentForm, EditStudentForm
from student.models import StudentAcademics, StudentInfo
from bs4 import BeautifulSoup
import requests
# Create your views here.
def add_student(request):
    form=AddStudentForm
    print('inform')
    return render(request,'add_student.html',{'form':form})

def add_student_save(request):
    
    if request.method != "POST":
        
        return HttpResponse('method not allowed')
    else:
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            
            roll_no=form.cleaned_data['RollNo']
            name=form.cleaned_data['Name']
            classname=form.cleaned_data['Class']
            school=form.cleaned_data['School']
            mobile=form.cleaned_data['Mobile']
            address=form.cleaned_data['Address']
            maths=form.cleaned_data['Maths']
            physics=form.cleaned_data['Physics']
            chemistry=form.cleaned_data['Chemistry']
            biology=form.cleaned_data['Biology']
            english=form.cleaned_data['English']


            try:
                s1=StudentInfo.objects.create(RollNo=roll_no,Name=name,Class=classname,School=school,
                                            Mobile=mobile,Address=address)
                StudentAcademics.objects.create(RollNo=s1,Maths=maths,Physics=physics,Chemistry=chemistry,
                                            Biology=biology,English=english)
                            
                messages.success(request,"Successfully Added Student")
                return HttpResponseRedirect(reverse('show-student'))
            except:
                messages.error(request,"Failed to Add Student")
                return HttpResponseRedirect(reverse('add-student'))

        else:
            
            form=AddStudentForm(request.POST)
            return render(request,'add_student.html',{'form':form})

def show_student(request):
    students=StudentInfo.objects.all()
    return render(request,'show_student.html',{'students':students})

def edit_student(request,student_id):
    request.session['student_id']=student_id
    student = StudentInfo.objects.get(RollNo=student_id)
    
    try:
        marks=StudentAcademics.objects.get(RollNo_id=student.RollNo)
    except:
        return HttpResponse('Marks Not Available ')
    form=EditStudentForm()
    
    form.fields['RollNo'].initial=student.RollNo
    form.fields['Name'].initial=student.Name
    form.fields['Class'].initial=student.Class
    form.fields['School'].initial=student.School
    form.fields['Mobile'].initial=student.Mobile
    form.fields['Address'].initial=student.Address
    form.fields['Maths'].initial=marks.Maths
    form.fields['Physics'].initial=marks.Physics
    form.fields['Chemistry'].initial=marks.Chemistry
    form.fields['Biology'].initial=marks.Biology
    form.fields['English'].initial=marks.English
    return render(request,'edit_student.html',{'form':form})


def edit_student_save(request):
    
    if request.method != "POST":
        
        return HttpResponse('method not allowed')
    else:
        
        form=EditStudentForm(request.POST,request.FILES)
        if form.is_valid():
            
            roll_no=form.cleaned_data['RollNo']
            name=form.cleaned_data['Name']
            classname=form.cleaned_data['Class']
            school=form.cleaned_data['School']
            mobile=form.cleaned_data['Mobile']
            address=form.cleaned_data['Address']
            maths=form.cleaned_data['Maths']
            physics=form.cleaned_data['Physics']
            chemistry=form.cleaned_data['Chemistry']
            biology=form.cleaned_data['Biology']
            english=form.cleaned_data['English']


            try:
                s1=StudentInfo.objects.get(RollNo=roll_no)
            
                s1.RollNo=roll_no
                s1.Name=name
                s1.Class=classname
                s1.School=school
                s1.Mobile=mobile
                s1.Address=address
                s1.save()
                m1=StudentAcademics.objects.get(RollNo=roll_no)
                m1.Maths=maths
                m1.Physics=physics
                m1.Chemistry=chemistry
                m1.Biology=biology
                m1.English=english
                m1.RollNo_id=roll_no
                m1.save()
                            
                messages.success(request,"Successfully Edited Student")
                return HttpResponseRedirect(reverse('show-student'))
            except:
                messages.error(request,"Failed to Edit Student")
                return HttpResponseRedirect(reverse('show-student'))

        else:
            
            form=AddStudentForm(request.POST)
            return render(request,'edit_student.html',{'form':form})

def delete_student(request,student_id):
    request.session['student_id']=student_id
    student = StudentInfo.objects.get(RollNo=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('show-student'))


def search_box(request):
    student=[]
    q=request.POST.get('table_search')
    
    queries=q.split(" ")
    for i in queries:
        students=StudentInfo.objects.filter(Name=i)
        for j in students:
            student.append(j)
    return render(request,'show_student.html',{'students':student})


def show_details(request,student_id):
    student=StudentInfo.objects.get(RollNo=student_id)
    academics=StudentAcademics.objects.get(RollNo_id=student_id)
    return render(request,'show_student_data.html',{'students':student,'academics':academics})

def login(request):
    return render(request,'login.html')


def dologin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
        
    else:
        
        user=authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        
        if user!=None:
            auth_login(request,user)
            return HttpResponseRedirect(reverse("show-student"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/login/")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def search_url(request):
    if request.method=="POST":

        url=request.POST.get('url')
        if "http://" not in url:
            req=requests.get('http://'+url)
        else:
            req=requests.get(url)            
        
        bs=BeautifulSoup(req.text,'html.parser')
        urls=[]
        for i in bs.find_all('a'):
            urls.append(i.get('href'))
        count=len(urls)
    else:
        urls=[]
        count=0
    return render(request,'show_website_url.html',{'urls':urls,'count':count})
