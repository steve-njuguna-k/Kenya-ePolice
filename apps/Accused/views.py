from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='Login')
def OfficerAccused(request):
    return render(request, 'Officer Accused.html')