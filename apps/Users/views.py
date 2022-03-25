from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from Accused.models import AccusedPerson
from Cases.models import Case
from Cells.models import Cell
from Courts.models import Court
from Users.forms import PasswordChangeForm, UpdateProfileForm, UpdateUserForm
from Users.models import Profile

# Create your views here.
def Home(request):
    return render(request, 'Index.html')

def Register(request):
    if request.method == 'POST':
        context = {'has_error': False}
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        national_id = request.POST['national_id']
        police_station = request.POST['police_station']
        county = request.POST['county']
        role = request.POST['role']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, '⚠️ Passwords Do Not Match! Try Again')
            return redirect('Register')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Officer Number Already Exists! Choose Another One')
            return redirect('Register')

        if Profile.objects.filter(national_id=national_id).exists():
            messages.error(request, '⚠️ National ID Number Already Exists! Choose Another One')
            return redirect('Register')

        if User.objects.filter(email=email).exists():
            messages.error(request, '⚠️ Email Address Already Exists! Choose Another One')
            return redirect('Register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        profile = Profile(user=user ,middle_name=middle_name, national_id=national_id, police_station=police_station, role=role, gender=gender, date_of_birth=date_of_birth, county=county)
        user.set_password(password1)
        user.is_active = True
        profile.save()
        user.save()

        if not context['has_error']:
            messages.success(request, '✅ Regristration Successful!')
            return redirect('Register')

    return render(request, 'Register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if not User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Officer Number Does Not Exist! Choose Another One')
            return redirect('Login')

        if user is None:
            messages.error(request, '⚠️ Officer Number/Password Is Incorrect or Account Is Not Activated!! Please Try Again')
            return redirect('Login')

        if user is not None:
            login(request, user)
            return redirect('OfficerDashboard')

    return render(request, 'Login.html')

@login_required(login_url='Login')
def Logout(request):
    logout(request)
    messages.success(request, ('✅ You Have Successfully Logged Out!'))
    return redirect('Login')

@login_required(login_url='Login')
def OfficerSettings(request):
    username = request.user
    profile_details = Profile.objects.get(user=username.id)
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, '✅ Your Password Has Been Updated Successfully!')
            return redirect("OfficerProfile")
        else:
            messages.error(request, "⚠️ Your Password Wasn't Updated!")
            return redirect("OfficerSettings")
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)
    
    return render(request, "Officer Settings.html", {'form': form, 'profile_details':profile_details})

@login_required(login_url='Login')
def OfficerEditProfile(request):
    user = request.user
    profile_details = Profile.objects.get(user = user.id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            profile_picture = profile_form.cleaned_data['profile_picture']
            middle_name = profile_form.cleaned_data['middle_name']
            bio = profile_form.cleaned_data['bio']
            national_id = profile_form.cleaned_data['national_id']
            date_of_birth = profile_form.cleaned_data['date_of_birth']
            police_station = profile_form.cleaned_data['police_station']
            gender = profile_form.cleaned_data['gender']
            role = profile_form.cleaned_data['role']
            county = profile_form.cleaned_data['county']

            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            username = user_form.cleaned_data['username']

            user.username = username
            user.first_name = first_name
            user.last_name = last_name

            profile_details.national_id = national_id
            profile_details.bio = bio
            profile_details.profile_picture = profile_picture
            profile_details.middle_name = middle_name
            profile_details.date_of_birth = date_of_birth
            profile_details.police_station = police_station
            profile_details.gender = gender
            profile_details.role = role
            profile_details.county = county

            user.save()
            profile_details.save()
            messages.success(request, '✅ Your Profile Details Has Been Updated Successfully!')
            return redirect('OfficerProfile')
        else:
            messages.error(request, "⚠️ Your Profile Wasn't Updated!")
            return redirect('OfficerEditProfile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'Officer Edit Profile.html', {'user_form': user_form, 'profile_form': profile_form, 'profile_details':profile_details})

@login_required(login_url='Login')
def OfficerProfile(request):
    profile = request.user
    profile_details = Profile.objects.get(user = profile.id)
    return render(request, 'Officer Profile.html', {'profile':profile, 'profile_details':profile_details})

@login_required(login_url='Login')
def OfficerDashboard(request):
    username = request.user
    profile = Profile.objects.get(user=username.id)
    accused = AccusedPerson.objects.filter(created_by=profile.id).order_by('-date_created').all()
    cases = Case.objects.filter(created_by=profile.id).order_by('-date_created').all()
    courts = Court.objects.filter(created_by=profile.id).order_by('-date_created').all()
    cells = Cell.objects.filter(created_by=profile.id).order_by('-date_created').all()
    return render(request, 'Officer Dashboard.html', {'accused':accused, 'cases':cases, 'courts':courts, 'cells':cells})

def Search(request):
    if request.method == 'POST':
        search = request.POST['Search']
        accused_first_name = AccusedPerson.objects.filter(first_name__icontains = search).all()
        accused_middle_name = AccusedPerson.objects.filter(middle_name__icontains = search).all()
        accused_last_name = AccusedPerson.objects.filter(last_name__icontains = search).all()
        return render(request, 'Search Results.html', {'search':search, 'accused_first_name':accused_first_name, 'accused_middle_name':accused_middle_name, 'accused_last_name':accused_last_name})
    else:
        return render(request, 'Search Results.html')