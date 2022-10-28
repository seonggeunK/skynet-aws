from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.

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
    return redirect("/works")

