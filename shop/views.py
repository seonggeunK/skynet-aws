from django.shortcuts import render
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

def workReg(request):
    print("workReg 함수입니다.")
    return render(request, "work-reg.html")






