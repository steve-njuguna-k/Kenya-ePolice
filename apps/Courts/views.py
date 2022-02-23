from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.Accused.models import AccusedPerson
from apps.Courts.forms import AddCourtInfoForm, EditCourtInfoForm
from apps.Courts.models import Court
from apps.Cases.models import Profile

# Create your views here.
@login_required(login_url='Login')
def OfficerCourtInfo(request):
    form = AddCourtInfoForm()
    courts = Court.objects.all().order_by('-date_created')
    return render(request, 'Officer Court Info.html', {'courts':courts, 'form':form})

def AddCourtInfo(request):
    profile = request.user.profile
    form = AddCourtInfoForm()
    if request.method == 'POST':
        form = AddCourtInfoForm(request.POST)

        if form.is_valid():
            court_number = form.cleaned_data['court_number']
            accused_person = form.cleaned_data['accused_person']
            court = form.cleaned_data['court']
            court_verdict = form.cleaned_data['court_verdict']
            scheduled_on = form.cleaned_data['scheduled_on']

            accused_person_obj = AccusedPerson.objects.get(pk=int(accused_person))
            new_court = Court(court_number = court_number, accused_person = accused_person_obj, court = court, court_verdict = court_verdict, scheduled_on = scheduled_on, created_by=profile)
            new_court.save()
            messages.success(request, '✅ Court Record Successfully Created!')
            return redirect('OfficerCourtInfo')
        else:
            messages.error(request, '⚠️ Court Record Was Not Created!')
            return redirect('OfficerCourtInfo')
    else:
        form = AddCourtInfoForm()
    return redirect('OfficerCourtInfo')

def EditCourtInfo(request, id):
    court = Court.objects.get(id=id)

    if request.method == 'POST':
        context = {'has_error': False}
        court_number = request.POST['court_number']
        accused_person = request.POST['accused_person']
        court = request.POST['court']
        court_verdict = request.POST['court_verdict']
        scheduled_on = request.POST['scheduled_on']

        court.court_number = court_number
        court.accused_person = AccusedPerson.objects.get(pk=int(accused_person))
        court.court = court
        court.court_verdict = court_verdict
        court.scheduled_on = scheduled_on
        court.created_by = request.user.profile

        if not context['has_error']:
            court.save()
            messages.success(request, '✅ Court Record Successfully Updated!')
            return redirect('OfficerCourtInfo')
                
        else:
            messages.error(request, '⚠️ Court Record Was Not Updated!')
            return redirect('OfficerCourtInfo')

    return redirect('OfficerCourtInfo')

def ViewCourtInfoDetails(request, id):
    court_details = Court.objects.get(id=id)
    return render(request, 'Officer Cases.html', {'court_details':court_details})

def DeleteCourtInfo(request, id):
    court_details = Court.objects.get(id=id)
    court_details.delete()
    messages.success(request, '✅ Court Record Successfully Deleted!')
    return redirect('OfficerCourtInfo')