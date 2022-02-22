from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.Accused.models import AccusedPerson
from apps.Cases.forms import AddCaseForm
from apps.Cases.models import Case
from apps.Users.models import Profile

# Create your views here.
@login_required(login_url='Login')
def OfficerCases(request):
    form = AddCaseForm()
    cases = Case.objects.all().order_by('-date_created')
    return render(request, 'Officer Cases.html', {'cases':cases, 'form':form})

def AddCase(request):
    profile = request.user
    form = AddCaseForm()
    if request.method == 'POST':
        form = AddCaseForm(request.POST)

        if form.is_valid():
            case_number = form.cleaned_data['case_number']
            accused_person = form.cleaned_data['accused_person']
            cause_of_arrest = form.cleaned_data['cause_of_arrest']
            crime_category = form.cleaned_data['crime_category']
            arrest_location = form.cleaned_data['arrest_location']
            police_station = form.cleaned_data['police_station']
            county = form.cleaned_data['county']
            case_started_on = form.cleaned_data['case_started_on']
            case_concluded_on = form.cleaned_data['case_concluded_on']
            case_status = form.cleaned_data['case_status']

            accused_person_obj = AccusedPerson.objects.get(pk=int(accused_person))
            police_station_member = Profile.objects.filter(user = profile, police_station = police_station)

            if not police_station_member:
                messages.error(request, "⚠️ You Must Choose Your Assigned Police Station!")
                return redirect('OfficerCases')

            else:
                accused_person_obj = AccusedPerson.objects.get(pk=int(accused_person))
                print(accused_person_obj)
                new_case = Case(case_number = case_number, accused_person = accused_person_obj, cause_of_arrest = cause_of_arrest, crime_category = crime_category, arrest_location = arrest_location, county=county, case_started_on=case_started_on, case_concluded_on=case_concluded_on, case_status=case_status, created_by=profile)
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
    person = Case.objects.get(id=id)
    print(person)
    if request.method == 'POST':
        context = {'has_error': False}
        arrest_number = request.POST['arrest_number']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        national_id = request.POST['national_id']
        profile_picture = request.FILES['profile_picture']
        arrest_status = request.POST['arrest_status']
        arrested_on = request.POST['arrested_on']

        person.arrest_number = arrest_number
        person.first_name = first_name
        person.middle_name = middle_name
        person.last_name = last_name
        person.date_of_birth = date_of_birth
        person.gender = gender
        person.national_id = national_id
        person.profile_picture = profile_picture
        person.arrest_status = arrest_status
        person.arrested_on = arrested_on
        person.created_by = request.user

        if not context['has_error']:
            person.save()
            messages.success(request, '✅ Case Record Successfully Updated!')
            return redirect('OfficerCases')
        
        else:
            messages.error(request, '⚠️ Case Record Was Not Updated!')
            return redirect('OfficerCases')

    return redirect('OfficerCases')

def ViewCaseDetails(request, id):
    person_details = Case.objects.get(id=id)
    return render(request, 'Officer Cases.html', {'person_details':person_details})

def DeleteCase(request, id):
    person_details = Case.objects.get(id=id)
    person_details.delete()
    messages.success(request, '✅ Case Record Successfully Deleted!')
    return redirect('OfficerCases')