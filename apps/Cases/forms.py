from django import forms
from apps.Accused.models import AccusedPerson
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

class AddCaseForm(forms.Form):
    case_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'case_number', 'class': 'form-control mb-4', 'name': 'case_number', 'placeholder': 'Case Number'}))
    accused_person = forms.ChoiceField(required=True, widget=forms.Select(attrs={'id': 'accused_person', 'class': 'form-control mb-4', 'name': 'accused_person', 'placeholder': 'Accused Person'}))
    cause_of_arrest = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'cause_of_arrest', 'class': 'form-control mb-4', 'name': 'cause_of_arrest', 'placeholder': 'Cause of Arrest'}))
    crime_category = forms.ChoiceField(choices=CRIME, required=True, widget=forms.Select(attrs={'id': 'crime_category', 'class': 'form-control mb-4', 'name': 'crime_category', 'placeholder': 'Category'}))
    arrest_location = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'arrest_location', 'class': 'form-control mb-4', 'name': 'arrest_location', 'placeholder': 'Arrest Location'}))
    police_station = forms.ChoiceField(choices=STATIONS, required=True, widget=forms.Select(attrs={'id': 'police_station', 'class': 'form-control mb-4', 'name': 'police_station', 'placeholder': 'Police Station'}))
    county = forms.ChoiceField(choices=COUNTIES, required=True, widget=forms.Select(attrs={'id': 'county', 'class': 'form-control mb-4', 'name': 'county', 'placeholder': 'County'}))
    case_started_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'case_started_on', 'class': 'form-control mb-4', 'name': 'case_started_on', 'placeholder': 'Case Started On'}))
    case_concluded_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'case_concluded_on', 'class': 'form-control mb-4', 'name': 'case_concluded_on', 'placeholder': 'Case Concluded On'}))
    case_status = forms.ChoiceField(choices=CASE_STATUS, required=True, widget=forms.Select(attrs={'type': 'date', 'id': 'case_status', 'class': 'form-control mb-4', 'name': 'case_status', 'placeholder': 'Case Status'}))

    def __init__(self, *args, **kwargs):
        super(AddCaseForm, self).__init__(*args, **kwargs)
        self.fields['accused_person'].choices = [(e.pk, f"{e.first_name}" + ' ' + f"{e.middle_name}" + ' ' + f"{e.last_name}") for e in AccusedPerson.objects.all()]

    class Meta:
        model = Case
        fields = ['case_number', 'accused_person', 'cause_of_arrest', 'crime_category', 'arrest_location', 'police_station', 'county', 'case_started_on', 'case_concluded_on', 'case_status']


class EditCaseForm(forms.Form):
    case_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'case_number', 'class': 'form-control mb-4', 'name': 'case_number', 'placeholder': 'Case Number', 'readonly':'readonly'}))
    accused_person = forms.ChoiceField(required=True, widget=forms.Select(attrs={'id': 'accused_person', 'class': 'form-control mb-4', 'name': 'accused_person', 'placeholder': 'Accused Person'}))
    cause_of_arrest = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'cause_of_arrest', 'class': 'form-control mb-4', 'name': 'cause_of_arrest', 'placeholder': 'Cause of Arrest'}))
    crime_category = forms.ChoiceField(choices=CRIME, required=True, widget=forms.Select(attrs={'id': 'crime_category', 'class': 'form-control mb-4', 'name': 'crime_category', 'placeholder': 'Category'}))
    arrest_location = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'arrest_location', 'class': 'form-control mb-4', 'name': 'arrest_location', 'placeholder': 'Arrest Location'}))
    police_station = forms.ChoiceField(choices=STATIONS, required=True, widget=forms.Select(attrs={'id': 'police_station', 'class': 'form-control mb-4', 'name': 'police_station', 'placeholder': 'Police Station'}))
    county = forms.ChoiceField(choices=COUNTIES, required=True, widget=forms.Select(attrs={'id': 'county', 'class': 'form-control mb-4', 'name': 'county', 'placeholder': 'County'}))
    case_started_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'case_started_on', 'class': 'form-control mb-4', 'name': 'case_started_on', 'placeholder': 'Case Started On'}))
    case_concluded_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'case_concluded_on', 'class': 'form-control mb-4', 'name': 'case_concluded_on', 'placeholder': 'Case Concluded On'}))
    case_status = forms.ChoiceField(choices=CASE_STATUS, required=True, widget=forms.Select(attrs={'type': 'date', 'id': 'case_status', 'class': 'form-control mb-4', 'name': 'case_status', 'placeholder': 'Case Status'}))

    def __init__(self, *args, **kwargs):
        super(EditCaseForm, self).__init__(*args, **kwargs)
        self.fields['accused_person'].choices = [(e.pk, f"{e.first_name}" + ' ' + f"{e.middle_name}" + ' ' + f"{e.last_name}") for e in AccusedPerson.objects.all()]

    class Meta:
        model = Case
        fields = ['case_number', 'accused_person', 'cause_of_arrest', 'crime_category', 'arrest_location', 'police_station', 'county', 'case_started_on', 'case_concluded_on', 'case_status']
