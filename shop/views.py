from django.shortcuts import render
from shop.models import Shop
from django.shortcuts import redirect

from django.core.files.storage import FileSystemStorage

import datetime
import random
import sys, os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import joblib

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# def index(request):
#     return HttpResponse('''
#     <html>
#         <body>
#         <h1> 안녕하세요 ! </h1>
#         </body>
#     </html>
#     ''')

def index(request):
    print("index")
    category = 0
    categoryName = 'All'

    rsshop = Shop.objects.all()

    return render(request, "index.html", {
        "rsshop": rsshop,
        "category": category,
        "categoryName": categoryName,

    })


def ml(request):
    print("login")
    return render(request, "ml.html")


def mlPro(request):
    print("loginPro")
    age = request.POST['age']
    sex = request.POST['sex']
    occupation = request.POST['occupation']
    hobby = request.POST['hobby']

    arr = np.array([[age, sex, occupation, hobby]], dtype=int)

    # 모델 불러오기
    model = joblib.load('shop/shopknn.pkl')
    # 예측
    pred = model.predict(arr)
    print('pred : {}'.format(pred))
    # All
    # Fashion
    # Beauty
    # Automotive
    # Sports
    categoryName = 'All'
    if pred == 1:
        categoryName = 'Fashion'
    elif pred == 2:
        categoryName = 'Beauty'
    elif pred == 3:
        categoryName = 'Automotive'
    elif pred == 4:
        categoryName = 'Sports'


    rsshop = Shop.objects.all()

    return render(request, "works.html", {
        'rsshop': rsshop,
        'category': pred,
        'categoryName': categoryName
    })


def about(request):
    print("about")
    return render(request, "about.html")


def services(request):
    print("services")
    return render(request, "services.html")


def contact(request):
    print("contact")
    return render(request, "contact.html")


def works(request):
    print("works")
    category = 0
    categoryName = 'All'
    rsshop = Shop.objects.all()

    return render(request, "works.html", {
        'rsshop': rsshop,
        'category': category,
        'categoryName': categoryName

    })


def workSingle(request, no):
    print("workSigle")
    shop = Shop.objects.get(no=no)
    return render(request, "work-single.html", {
        'shop': shop
    })


def workReg(request):
    print("workReg")
    return render(request, "work-reg.html")


def workPro(request):
    no = request.POST['no']
    title = request.POST['title']
    category = request.POST['category']
    summary = request.POST['summary']
    subject = request.POST['subject']
    contents = request.POST['contents']

    dt_now = datetime.datetime.now()
    str_date = dt_now.strftime('%Y_%m_%d_%H%M_%f')
    if 'ufile' in request.FILES:
        uploaded_file = request.FILES['ufile']
        org_file_name = uploaded_file.name
        print('{}'.format(org_file_name))
        name_ext = os.path.splitext(org_file_name)[1]
        new_file_name = 'shop' + str_date + '_' + str(random.randint(1000000000, 9999999999))
        new_file_location = 'shop/static/upload/photos'
        fs = FileSystemStorage(location=new_file_location)

        name = fs.save(new_file_name + name_ext, uploaded_file)

    if no in (None, ''):
        rows = Shop.objects.create(
            title=title,
            category=category,
            summary=summary,
            subject=subject,
            contents=contents,
            org_file_name=org_file_name,
            file_name=name,
            file_location=new_file_location
        )
    else:
        shop = Shop.objects.get(no=no)
        shop.title = title
        shop.category = category
        shop.summary = summary
        shop.subject = subject
        shop.contents = contents
        if 'ufile' in request.FILES:
            shop.org_file_name = org_file_name
            shop.file_name = name
            shop.file_location = new_file_location
        shop.save()
    return redirect('/works')


def workModify(request, no):
    print("workModify")
    shop = Shop.objects.get(no=no)
    return render(request, "work-reg.html", {
        'shop': shop
    })


def workRemove(request, no):
    Shop.objects.filter(no=no).delete()
    return redirect('/works')
