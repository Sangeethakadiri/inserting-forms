from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hai(request):
    if request.method=='POST':
        name=request.POST['un']
        password=request.POST['pw']
        print(name)
        print(Password)
        return HttpResponse('hai is submitted')


    return render(request,'hai.html')