from django import forms
from apps.Accused.models import ARREST_STATUS, GENDER, AccusedPerson
from apps.Cases.models import Case

STATIONS = [
    ("Central Police Station", "Central Police Station"),
    ("Kilimani Police Station", "Kilimani Police Station"),
    ("Embakasi Police Station", "Embakasi Police Station"),
    ("Lang'ata Police Station", "Lang'ata Police Station"),
    ("Ong'ata Rongai Police Station", "Ong'ata Rongai Police Station"),
    ("Buruburu Police Station", "Buruburu Police Station"),
    ("Kasarani Police Station", "Kasarani Police Station"),
    ("Parklands Police Station", "Parklands Police Station"),
    ("Pangani Police Station", "Pangani Police Station"),
    ("Muthaiga Police Station", "Muthaiga Police Station"),
]

COUNTIES = [
    ('Baringo', ('Baringo')),
    ('Bomet', ('Bomet')),
    ('Bungoma ', ('Bungoma ')),
    ('Busia', ('Busia')),
    ('Elgeyo Marakwet', ('Elgeyo Marakwet')),
    ('Embu', ('Embu')),
    ('Garissa', ('Garissa')),
    ('Homa Bay', ('Homa Bay')),
    ('Isiolo', ('Isiolo')),
    ('Kajiado', ('Kajiado')),
    ('Kakamega', ('Kakamega')),
    ('Kericho', ('Kericho')),
    ('Kiambu', ('Kiambu')),
    ('Kilifi', ('Kilifi')),
    ('Kirinyaga', ('Kirinyaga')),
    ('Kisii', ('Kisii')),
    ('Kisumu', ('Kisumu')),
    ('Kitui', ('Kitui')),
    ('Kwale', ('Kwale')),
    ('Laikipia', ('Laikipia')),
    ('Lamu', ('Lamu')),
    ('Machakos', ('Machakos')),
    ('Makueni', ('Makueni')),
    ('Mandera', ('Mandera')),
    ('Meru', ('Meru')),
    ('Migori', ('Migori')),
    ('Marsabit', ('Marsabit')),
    ('Mombasa', ('Mombasa')),
    ('Muranga', ('Muranga')),
    ('Nairobi', ('Nairobi')),
    ('Nakuru', ('Nakuru')),
    ('Nandi', ('Nandi')),
    ('Narok', ('Narok')),
    ('Nyamira', ('Nyamira')),
    ('Nyandarua', ('Nyandarua')),
    ('Nyeri', ('Nyeri')),
    ('Samburu', ('Samburu')),
    ('Siaya', ('Siaya')),
    ('Taita Taveta', ('Taita Taveta')),
    ('Tana River', ('Tana River')),
    ('Tharaka Nithi', ('Tharaka Nithi')),
    ('Trans Nzoia', ('Trans Nzoia')),
    ('Turkana', ('Turkana')),
    ('Uasin Gishu', ('Uasin Gishu')),
    ('Vihiga', ('Vihiga')),
    ('Wajir', ('Wajir')),
    ('West Pokot', ('West Pokot')),
]

CRIME = [
    ('Arson', ('Arson')),
    ('Armed Robbery', ('Armed Robbery')),
    ('Assault', ('Assault')),
    ('Burglary', ('Burglary')),
    ('Carjacking', ('Carjacking')),
    ('Cattle Rustling', ('Cattle Rustling')),
    ('Corruption', ('Corruption')),
    ('Drug Abuse', ('Drug Abuse')),
    ('Drug Trafficking', ('Drug Trafficking')),
    ('Embezzlement', ('Embezzlement')),
    ('Fraud', ('Fraud')),
    ('Homicide', ('Homicide')),
    ('Human trafficking', ('Human trafficking')),
    ('Kidnapping', ('Kidnapping')),
    ('Mob Justice', ('Mob Justice')),
    ('Money Laundering', ('Money Laundering')),
    ('Massive Looting', ('Massive Looting')),
    ('Petty Theft', ('Petty Theft')),
    ('Pickpocketing', ('Pickpocketing')),
    ('Rape', ('Rape')),
    ('Terrorism', ('Terrorism')),
]

CASE_STATUS = [
    ('Not Started', ('Not Started')),
    ('Ongoing', ('Ongoing')),
    ('Complete', ('Complete')),
]

class AddAccusedForm(forms.ModelForm):
    arrest_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'arrest_number', 'class': 'form-control mb-4', 'name': 'arrest_number', 'placeholder': 'Arrest Number'}))
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'first_name', 'class': 'form-control mb-4', 'name': 'first_name', 'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'middle_name', 'class': 'form-control mb-4', 'name': 'middle_name', 'placeholder': 'Middle Name'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'last_name', 'class': 'form-control mb-4', 'name': 'last_name', 'placeholder': 'Last Name'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'date_of_birth', 'class': 'form-control mb-4', 'name': 'date_of_birth', 'placeholder': 'Date of Birth'}))
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={'id': 'gender', 'class': 'form-control mb-4', 'name': 'gender', 'placeholder': 'Gender'}))
    national_id = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'national_id', 'class': 'form-control mb-4', 'name': 'national_id', 'placeholder': 'Arrest Location'}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control file'}))
    arrest_status = forms.ChoiceField(choices=ARREST_STATUS, required=True, widget=forms.Select(attrs={'type': 'date', 'id': 'case_status', 'class': 'form-control mb-4', 'name': 'case_status', 'placeholder': 'Case Status'}))
    arrested_on = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'id': 'arrested_on', 'class': 'form-control mb-4', 'name': 'arrested_on', 'placeholder': 'Arrested On'}))

    class Meta:
        model = AccusedPerson
        fields = ['arrest_number', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'national_id', 'profile_picture', 'arrest_status', 'arrested_on']


class EditAccusedForm(forms.ModelForm):
    arrest_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'arrest_number', 'class': 'form-control mb-4', 'name': 'arrest_number', 'placeholder': 'Arrest Number'}))
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'first_name', 'class': 'form-control mb-4', 'name': 'first_name', 'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'middle_name', 'class': 'form-control mb-4', 'name': 'middle_name', 'placeholder': 'Middle Name'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'last_name', 'class': 'form-control mb-4', 'name': 'last_name', 'placeholder': 'Last Name'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'date_of_birth', 'class': 'form-control mb-4', 'name': 'date_of_birth', 'placeholder': 'Date of Birth'}))
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={'id': 'gender', 'class': 'form-control mb-4', 'name': 'gender', 'placeholder': 'Gender'}))
    national_id = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'national_id', 'class': 'form-control mb-4', 'name': 'national_id', 'placeholder': 'Arrest Location'}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control file'}))
    arrest_status = forms.ChoiceField(choices=ARREST_STATUS, required=True, widget=forms.Select(attrs={'type': 'date', 'id': 'case_status', 'class': 'form-control mb-4', 'name': 'case_status', 'placeholder': 'Case Status'}))
    arrested_on = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'id': 'arrested_on', 'class': 'form-control mb-4', 'name': 'arrested_on', 'placeholder': 'Arrested On'}))

    class Meta:
        model = AccusedPerson
        fields = ['arrest_number', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'national_id', 'profile_picture', 'arrest_status', 'arrested_on']
