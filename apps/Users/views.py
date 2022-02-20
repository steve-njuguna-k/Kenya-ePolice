from django.shortcuts import render

# Create your views here.
def GetStarted(request):
    return render(request, 'Get Started.html')