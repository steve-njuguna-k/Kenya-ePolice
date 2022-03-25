import imp
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Docs.models import Docs

# Create your views here.
@login_required(login_url='Login')
def OfficerDocs(request):
    all_docs = Docs.objects.all().order_by('title')
    return render(request, 'Officer Docs.html', {'all_docs':all_docs})