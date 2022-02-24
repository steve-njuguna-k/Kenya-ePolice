from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.Shifts.models import Shift

# Create your views here.
@login_required(login_url='Login')
def OfficerShifts(request):
    current_user = request.user.profile
    shifts = Shift.objects.filter(id=current_user.id)
    return render(request, 'Officer Shifts.html', {'shifts':shifts})