from django.shortcuts import render

# Create your views here.
def GetStartedRegister(request):
    return render(request, 'Get Started Register.html')

def GetStartedLogin(request):
    return render(request, 'Get Started Login.html')