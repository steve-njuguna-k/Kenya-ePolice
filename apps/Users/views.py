from django.shortcuts import render

# Create your views here.
def GetStartedRegister(request):
    return render(request, 'Get Started Register.html')

def GetStartedLogin(request):
    return render(request, 'Get Started Login.html')

def OCSRegister(request):
    return render(request, 'OCS Register.html')

def OCSLogin(request):
    return render(request, 'OCS Login.html')

def OfficerRegister(request):
    return render(request, 'Police Officer Register.html')

def OfficerLogin(request):
    return render(request, 'Police Officer Login.html')

def Home(request):
    return render(request, 'Index.html')