from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import update_session_auth_hash
from apps.Users.forms import PasswordChangeForm, UpdateProfileForm, UpdateUserForm
from apps.Users.models import Profile
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from Core import settings
import threading

# Create your views here.
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = '[KENYA ePOLICE] Activate Your Account'
    email_body = render_to_string('Account Activation Email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
    from_email=settings.EMAIL_FROM_USER, to=[user.email])

    if not settings.TESTING:
        EmailThread(email).start()

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
        user.is_active = False
        profile.save()
        user.save()

        if not context['has_error']:
            send_activation_email(user, request)
            messages.success(request, '✅ Regristration Successful! An Activation Link Has Been Sent To Your Email')
            return redirect('Register')

    return render(request, 'Register.html')

def ActivateAccount(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        messages.success(request, ('✅ Email Verified! You can now Log in'))
        return redirect('Login')
    else:
        messages.error(request, ('⚠️ The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('Login')

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
            user_obj = User.objects.get(username=username)
            user_id = user_obj.id
            profile_obj = Profile.objects.filter(user=user_id)
            for item in profile_obj:
                if item.role == 'Police Officer':
                    login(request, user)
                    return redirect('OfficerDashboard')
                else:
                    login(request, user)
                    return redirect('OCSDashboard')

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
def OCSDashboard(request):
    return render(request, 'OCS Dashboard.html')

@login_required(login_url='Login')
def OfficerDashboard(request):
    return render(request, 'Officer Dashboard.html')

def Home(request):
    return render(request, 'Index.html')