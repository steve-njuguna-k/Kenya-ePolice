from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.Accused.models import AccusedPerson
from apps.Cells.forms import AddCellForm, EditCellForm
from apps.Cells.models import Cell
from apps.Users.models import Profile

# Create your views here.
@login_required(login_url='Login')
def OfficerCells(request):
    form = AddCellForm()
    profile = request.user
    cells = Cell.objects.filter(created_by=profile.id).all().order_by('-date_created')
    return render(request, 'Officer Cells.html', {'cells':cells, 'form':form})

def AddCellInfo(request):
    profile = request.user.profile
    form = AddCellForm()
    if request.method == 'POST':
        form = AddCellForm(request.POST)

        if form.is_valid():
            cell_number = form.cleaned_data['cell_number']
            accused_person = form.cleaned_data['accused_person']
            cell_status = form.cleaned_data['cell_status']
            occupied_on = form.cleaned_data['occupied_on']
            vaccated_on = form.cleaned_data['vaccated_on']

            accused_person_obj = AccusedPerson.objects.get(pk=int(accused_person))
            new_cell_info = Cell(cell_number = cell_number, accused_person = accused_person_obj, cell_status = cell_status, occupied_on = occupied_on, vaccated_on = vaccated_on, created_by=profile)
            new_cell_info.save()
            messages.success(request, '✅ Cell Record Successfully Created!')
            return redirect('OfficerCells')
        else:
            messages.error(request, '⚠️ Cell Record Was Not Created!')
            return redirect('OfficerCells')
    else:
        form = AddCellForm()
    return redirect('OfficerCells')

def EditCellInfo(request, id):
    cell = Cell.objects.get(id=id)
    profile = request.user

    if request.method == 'POST':
        context = {'has_error': False}
        cell_number = request.POST['cell_number']
        accused_person = request.POST['accused_person']
        cell_status = request.POST['cell_status']
        occupied_on = request.POST['occupied_on']
        vaccated_on = request.POST['vaccated_on']

        cell.cell_number = cell_number
        cell.accused_person = AccusedPerson.objects.get(pk=int(accused_person))
        cell.cell_status = cell_status
        cell.occupied_on = occupied_on
        cell.vaccated_on = vaccated_on
        cell.created_by = request.user.profile

        if not context['has_error']:
            cell.save()
            messages.success(request, '✅ Cell Record Successfully Updated!')
            return redirect('OfficerCells')
            
        else:
            messages.error(request, '⚠️ Cell Record Was Not Updated!')
            return redirect('OfficerCells')

    return redirect('OfficerCells')

def ViewCellDetails(request, id):
    cell_details = Cell.objects.get(id=id)
    return render(request, 'Officer Cells.html', {'cell_details':cell_details})

def DeleteCellInfo(request, id):
    cell_details = Cell.objects.get(id=id)
    cell_details.delete()
    messages.success(request, '✅ Cell Record Successfully Deleted!')
    return redirect('OfficerCells')