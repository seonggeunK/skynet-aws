from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
# Create your views here.
import datetime
import os
import random

from shop.models import Shop


# def index(request):
#     return HttpResponse('''
#         <html>
#             <body>
#                 <h1> Hello Django! </h1>
#             </body>
#         </html>
#     ''')

def index(request):
    print("index 함수입니다.")
    return render(request, "index.html")

def about(request):
    print("about 함수입니다.")
    return render(request, "about.html")

def services(request):
    print("about 함수입니다.")
    return render(request, "services.html")

def works(request):
    print("works 함수입니다.")
    return render(request, "works.html")

def contact(request):
    print("contact 함수입니다.")
    return render(request, "contact.html")

def workReg(request):
    print("workReg 함수입니다.")
    return render(request, "work-reg.html")

def workPro(request):
    print("workReg 함수입니다.")
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
            shop.org_file_name = org_file_name,
            shop.file_name = name,
            shop.file_location = new_file_location
        shop.save()

    return redirect("/works")

