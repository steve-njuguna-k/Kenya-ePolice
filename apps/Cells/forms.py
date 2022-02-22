from django import forms
from apps.Accused.models import AccusedPerson
from apps.Cells.models import Cell

CELL_STATUS = [
    ('Occupied', ('Occupied')),
    ('Empty', ('Empty')),
]

class AddCellForm(forms.Form):
    cell_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'case_number', 'class': 'form-control mb-4', 'name': 'case_number', 'placeholder': 'Case Number'}))
    accused_person = forms.ChoiceField(required=True, widget=forms.Select(attrs={'id': 'accused_person', 'class': 'form-control mb-4', 'name': 'accused_person', 'placeholder': 'Accused Person'}))
    occupied_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'case_started_on', 'class': 'form-control mb-4', 'name': 'case_started_on', 'placeholder': 'Case Started On'}))
    vaccated_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'case_concluded_on', 'class': 'form-control mb-4', 'name': 'case_concluded_on', 'placeholder': 'Case Concluded On'}))
    cell_status = forms.ChoiceField(choices=CELL_STATUS, required=True, widget=forms.Select(attrs={'type': 'date', 'id': 'case_status', 'class': 'form-control mb-4', 'name': 'case_status', 'placeholder': 'Case Status'}))

    def __init__(self, *args, **kwargs):
        super(AddCellForm, self).__init__(*args, **kwargs)
        self.fields['accused_person'].choices = [(e.pk, f"{e.first_name}" + ' ' + f"{e.middle_name}" + ' ' + f"{e.last_name}") for e in AccusedPerson.objects.all()]

    class Meta:
        model = Cell
        fields = ['cell_number', 'accused_person', 'occupied_on', 'vaccated_on', 'cell_status']


class EditCellForm(forms.Form):
    cell_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'case_number', 'class': 'form-control mb-4', 'name': 'case_number', 'placeholder': 'Case Number'}))
    accused_person = forms.ChoiceField(required=True, widget=forms.Select(attrs={'id': 'accused_person', 'class': 'form-control mb-4', 'name': 'accused_person', 'placeholder': 'Accused Person'}))
    occupied_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'case_started_on', 'class': 'form-control mb-4', 'name': 'case_started_on', 'placeholder': 'Case Started On'}))
    vaccated_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'case_concluded_on', 'class': 'form-control mb-4', 'name': 'case_concluded_on', 'placeholder': 'Case Concluded On'}))
    cell_status = forms.ChoiceField(choices=CELL_STATUS, required=True, widget=forms.Select(attrs={'type': 'date', 'id': 'case_status', 'class': 'form-control mb-4', 'name': 'case_status', 'placeholder': 'Case Status'}))

    def __init__(self, *args, **kwargs):
        super(EditCellForm, self).__init__(*args, **kwargs)
        self.fields['accused_person'].choices = [(e.pk, f"{e.first_name}" + ' ' + f"{e.middle_name}" + ' ' + f"{e.last_name}") for e in AccusedPerson.objects.all()]

    class Meta:
        model = Cell
        fields = ['cell_number', 'accused_person', 'occupied_on', 'vaccated_on', 'cell_status']
