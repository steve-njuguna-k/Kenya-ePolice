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
from apps.Users.models import OCSProfile, OfficerProfile
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

def OfficerRegister(request):
    if request.method == 'POST':
        context = {'has_error': False}
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        id_number = request.POST['id_number']
        police_station = request.POST['police_station']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, '⚠️ Passwords Do Not Match! Try Again')
            return redirect('OfficerRegister')

        if User.objects.filter(username=username).exists():
            messages.error(request, '⚠️ Officer Number Already Exists! Choose Another One')
            return redirect('OfficerRegister')

        if User.objects.filter(email=email).exists():
            messages.error(request, '⚠️ Email Address Already Exists! Choose Another One')
            return redirect('OfficerRegister')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        profile = OfficerProfile(middle_name=middle_name, id_number=id_number, police_station=police_station)
        user.set_password(password1)
        user.is_active = False
        user.save()
        profile.save()

        if not context['has_error']:
            send_activation_email(user, request)
            messages.success(request, '✅ Regristration Successful! An Activation Link Has Been Sent To Your Email')
            return redirect('OfficerRegister')

    return render(request, 'Police Officer Register.html')

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
        return redirect('OfficerLogin')
    else:
        messages.error(request, ('⚠️ The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('OfficerLogin')

def GetStartedRegister(request):
    return render(request, 'Get Started Register.html')

def GetStartedLogin(request):
    return render(request, 'Get Started Login.html')

def OCSRegister(request):
    return render(request, 'OCS Register.html')

def OCSLogin(request):
    return render(request, 'OCS Login.html')


def OfficerLogin(request):
    return render(request, 'Police Officer Login.html')

def Home(request):
    return render(request, 'Index.html')