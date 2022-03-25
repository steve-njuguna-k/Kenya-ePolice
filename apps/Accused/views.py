from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from Accused.forms import AddAccusedForm, EditAccusedForm
from Accused.models import AccusedPerson
from Users.models import Profile

# Create your views here.
@login_required(login_url='Login')
def OfficerAccused(request):
    form = AddAccusedForm()
    username = request.user
    profile = Profile.objects.get(user=username.id)
    accused = AccusedPerson.objects.filter(created_by=profile).all()
    return render(request, 'Officer Accused.html', {'accused':accused, 'form':form})

def AddArrestedPerson(request):
    form = AddAccusedForm()
    if request.method == 'POST':
        form = AddAccusedForm(request.POST, request.FILES)
        if form.is_valid():
            context = {'has_error': False}
            arrest_number = form.cleaned_data['arrest_number']
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            national_id = form.cleaned_data['national_id']
            profile_picture = form.cleaned_data['profile_picture']
            arrest_status = form.cleaned_data['arrest_status']
            arrested_on = form.cleaned_data['arrested_on']

        if not context['has_error']:
            arrested_person = AccusedPerson(arrest_number=arrest_number, first_name=first_name, middle_name=middle_name, last_name=last_name, date_of_birth=date_of_birth, gender=gender, national_id=national_id, profile_picture=profile_picture, arrest_status=arrest_status, arrested_on=arrested_on, created_by=request.user.profile)
            arrested_person.save()
            messages.success(request, '✅ Arrest Record Successfully Created!')
            return redirect('OfficerAccused')
        
        else:
            messages.error(request, '⚠️ Arrest Record Was Not Created!')
            return redirect('OfficerAccused')

    return redirect('OfficerAccused')

def EditArrestedPerson(request, id):
    person = AccusedPerson.objects.get(id=id)
    if request.method == 'POST':
        form = EditAccusedForm(request.POST, request.FILES)

        if form.is_valid():
            arrest_number = form.cleaned_data['arrest_number']
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            national_id = form.cleaned_data['national_id']
            # profile_picture = form.cleaned_data['profile_picture']
            arrest_status = form.cleaned_data['arrest_status']
            arrested_on = form.cleaned_data['arrested_on']

            person.arrest_number = arrest_number
            person.first_name = first_name
            person.middle_name = middle_name
            person.last_name = last_name
            person.date_of_birth = date_of_birth
            person.gender = gender
            person.national_id = national_id
            # person.profile_picture = profile_picture
            person.arrest_status = arrest_status
            person.arrested_on = arrested_on
            person.created_by = request.user.profile

            person.save()
            messages.success(request, '✅ Arrest Record Successfully Updated!')
            return redirect('OfficerAccused')
        else:
            messages.error(request, "⚠️ Arrest Record Was Not Updated!")
            return redirect('OfficerAccused')
    else:
        form = EditAccusedForm(instance=request.user.profile)

    return redirect('OfficerAccused')

def ViewArrestedPersonDetails(request, id):
    person_details = AccusedPerson.objects.get(id=id)
    return render(request, 'Officer Accused.html', {'person_details':person_details})

def DeleteArrestedPersonDetails(request, id):
    person_details = AccusedPerson.objects.get(id=id)
    person_details.delete()
    messages.success(request, '✅ Arrest Record Successfully Deleted!')
    return redirect('OfficerAccused')