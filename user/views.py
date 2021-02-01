from django.shortcuts import render, redirect
from django.contrib import messages
from tables.models import *


# Create your views here.


def homeView(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    email = request.session['id']
    obj = userTbl.objects.filter(email=email)
    return render(request, 'user/master.html', {'obj': obj[0]})


def viewList(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    email = request.session['id']
    obj = userTbl.objects.filter(email=email)
    items = itemTbl.objects.filter(uId_id=request.session['uId'])
    if items.count() == 0:
        messages.success(request, "Grocery List is Empty")
        return redirect('http://127.0.0.1:8000/user/')

    if request.method == 'POST':
        dt = request.POST['filterDate']
        if dt == '':
            messages.success(request, "Invalid Filter Date")
            return redirect('http://127.0.0.1:8000/user/view/')

        items = itemTbl.objects.filter(uId_id=request.session['uId'], date=dt)
        if items.count() == 0:
            messages.success(request, "Item List is Empty")
            return redirect('http://127.0.0.1:8000/user/view/')
        else:
            return render(request, 'user/viewList.html', {'obj': obj[0], 'items': items})
    return render(request, 'user/viewList.html', {'obj': obj[0], 'items': items})


def addList(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    email = request.session['id']
    obj = userTbl.objects.filter(email=email)
    items = itemTbl.objects.filter(uId_id=request.session['uId'])
    if items.count() == 0:
        messages.success(request, "Grocery List is Empty")
        return redirect('http://127.0.0.1:8000/user/')

    if request.method == 'POST':
        uId = request.session['uId']
        name = request.POST['name']
        qty = request.POST['qty']
        status = request.POST['status']
        date = request.POST['date']

        db = itemTbl(uId_id=uId, name=name, qty=qty, status=status, date=date)
        db.save()
        messages.success(request, "Item Added")
        return render(request, 'user/add.html', {'obj': obj[0]})

    return render(request, 'user/add.html', {'obj': obj[0]})


def updateList(request, itemId):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    email = request.session['id']
    obj = userTbl.objects.filter(email=email)
    items = itemTbl.objects.filter(uId_id=request.session['uId'], itemId=itemId)
    if items.count() == 0:
        return redirect('http://127.0.0.1:8000/user/')

    if request.method == 'POST':
        name = request.POST['name']
        qty = request.POST['qty']
        status = request.POST['status']
        date = request.POST['date']

        db = itemTbl.objects.filter(itemId=itemId).update(name=name, qty=qty, status=status, date=date)
        messages.success(request, "Item Details Updated")
        return redirect('http://127.0.0.1:8000/user/view/')


    return render(request, 'user/update.html', {'obj': obj[0], 'item': items[0]})


def deleteList(request, itemId):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://127.0.0.1:8000/')

    email = request.session['id']
    obj = userTbl.objects.filter(email=email)
    items = itemTbl.objects.filter(uId_id=request.session['uId'], itemId=itemId)
    if items.count() == 0:
        return redirect('http://127.0.0.1:8000/user/')

    db = itemTbl.objects.filter(itemId=itemId).delete()
    #messages.success(request, "Item Details Deleted")

    return redirect('http://127.0.0.1:8000/user/view/')