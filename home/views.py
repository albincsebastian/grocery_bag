from django.shortcuts import render, redirect
from django.contrib import messages
from tables.models import *
# Create your views here.


def homeView(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]

    return render(request, 'home/master.html')


def signUp(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']

        obj = userTbl.objects.filter(email=email)
        if obj.count()>0:
            messages.success(request, 'Email Exists')
            return render(request, 'home/signup.html')

        db = userTbl(name=name, pwd=pwd, email=email)
        db.save()
        messages.success(request, 'Registration Successful')
        return redirect('http://127.0.0.1:8000/login/')

    return render(request, 'home/signup.html')


def login(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]

    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['psw']
        obj = userTbl.objects.filter(email=email, pwd=pwd)
        if obj.count() == 0:
            messages.success(request, 'Incorrect Username / Password')
            return render(request, 'home/login.html')
        else:
            request.session['id'] = obj[0].email
            request.session['uId'] = obj[0].uId
            return redirect('http://127.0.0.1:8000/user/')

    return render(request, 'home/login.html')