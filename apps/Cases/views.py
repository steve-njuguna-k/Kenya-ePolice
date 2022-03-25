from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.Accused.models import AccusedPerson
from apps.Cases.forms import AddCaseForm, EditCaseForm
from apps.Cases.models import Case

# Create your views here.
@login_required(login_url='Login')
def OfficerCases(request):
    form = AddCaseForm()
    profile = request.user
    cases = Case.objects.filter(created_by=profile.id).all().order_by('-date_created')
    return render(request, 'Officer Cases.html', {'cases':cases, 'form':form})

def AddCase(request):
    profile = request.user.profile
    form = AddCaseForm()
    if request.method == 'POST':
        form = AddCaseForm(request.POST)

        if form.is_valid():
            case_number = form.cleaned_data['case_number']
            accused_person = form.cleaned_data['accused_person']
            cause_of_arrest = form.cleaned_data['cause_of_arrest']
            crime_category = form.cleaned_data['crime_category']
            arrest_location = form.cleaned_data['arrest_location']
            case_started_on = form.cleaned_data['case_started_on']
            case_concluded_on = form.cleaned_data['case_concluded_on']
            case_status = form.cleaned_data['case_status']

            accused_person_obj = AccusedPerson.objects.get(pk=int(accused_person))

            accused_person_obj = AccusedPerson.objects.get(pk=int(accused_person))
            new_case = Case(case_number = case_number, accused_person = accused_person_obj, cause_of_arrest = cause_of_arrest, crime_category = crime_category, arrest_location = arrest_location, case_started_on=case_started_on, case_concluded_on=case_concluded_on, case_status=case_status, created_by=profile)
            new_case.save()
            messages.success(request, '✅ Case Record Successfully Created!')
            return redirect('OfficerCases')
        else:
            messages.error(request, '⚠️ Case Record Was Not Created!')
            return redirect('OfficerCases')
    else:
        form = AddCaseForm()
    return redirect('OfficerCases')

def EditCase(request, id):
    case = Case.objects.get(id=id)

    if request.method == 'POST':
        form = EditCaseForm(request.POST)

        if form.is_valid():
            context = {'has_error': False}
            case_number = form.cleaned_data['case_number']
            accused_person = form.cleaned_data['accused_person']
            cause_of_arrest = form.cleaned_data['cause_of_arrest']
            crime_category = form.cleaned_data['crime_category']
            arrest_location = form.cleaned_data['arrest_location']
            case_started_on = form.cleaned_data['case_started_on']
            case_concluded_on = form.cleaned_data['case_concluded_on']
            case_status = form.cleaned_data['case_status']

            case.case_number = case_number
            case.accused_person = AccusedPerson.objects.get(pk=int(accused_person))
            case.cause_of_arrest = cause_of_arrest
            case.crime_category = crime_category
            case.arrest_location = arrest_location
            case.case_started_on = case_started_on
            case.case_concluded_on = case_concluded_on
            case.case_status = case_status
            case.created_by = request.user.profile

            if not context['has_error']:
                case.save()
                messages.success(request, '✅ Case Record Successfully Updated!')
                return redirect('OfficerCases')
                
        else:
            messages.error(request, '⚠️ Case Record Was Not Updated!')
            return redirect('OfficerCases')

    else:
        form = EditCaseForm(instance=request.user.profile)

    return redirect('OfficerCases')

def ViewCaseDetails(request, id):
    case_details = Case.objects.get(id=id)
    return render(request, 'Officer Cases.html', {'case_details':case_details})

def DeleteCase(request, id):
    case_details = Case.objects.get(id=id)
    case_details.delete()
    messages.success(request, '✅ Case Record Successfully Deleted!')
    return redirect('OfficerCases')