from django import forms
from apps.Accused.models import AccusedPerson

GENDER = [
    ('Male', ('Male')),
    ('Female', ('Female')),
]

ARREST_STATUS = [
    ('Free', ('Free')),
    ('Convicted', ('Convicted')),
    ('In Cutody', ('In Cutody')),
    ('Out On Bond', ('Out On Bond')),
    ('Out On Cash Bail', ('Out On Cash Bail')),
]

class UpdateArrestedPersonForm(forms.ModelForm):
    arrest_number = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Arrest Number', 'readonly':'readonly'}))
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'First Name', 'readonly':'readonly'}))
    middle_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Middle Name', 'readonly':'readonly'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Last Name', 'readonly':'readonly'}))
    date_of_birth = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Date Of Birth', 'readonly':'readonly'}))
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4', 'readonly':'readonly'}))
    national_id = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'National ID', 'readonly':'readonly'}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-4'}))
    arrest_status = forms.ChoiceField(choices=ARREST_STATUS, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4'}))

    class Meta:
        model = AccusedPerson
        fields = ['arrest_number', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'national_id', 'profile_picture', 'arrest_status']