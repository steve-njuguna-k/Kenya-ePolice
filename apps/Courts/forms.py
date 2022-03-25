from django import forms
from Accused.models import AccusedPerson
from Courts.models import COURTS, VERDICT, Court

class AddCourtInfoForm(forms.Form):
    court_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'court_number', 'class': 'form-control mb-4', 'name': 'court_number', 'placeholder': 'Court Number'}))
    accused_person = forms.ChoiceField(required=True, widget=forms.Select(attrs={'id': 'accused_person', 'class': 'form-control mb-4', 'name': 'accused_person', 'placeholder': 'Accused Person'}))
    court = forms.ChoiceField(choices=COURTS, required=True, widget=forms.Select(attrs={'id': 'court', 'class': 'form-control mb-4', 'name': 'court', 'placeholder': 'Court'}))
    court_verdict = forms.ChoiceField(choices=VERDICT, required=True, widget=forms.Select(attrs={'id': 'court_verdict', 'class': 'form-control mb-4', 'name': 'court_verdict', 'placeholder': 'Verdict'}))
    scheduled_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'scheduled_on', 'class': 'form-control mb-4', 'name': 'scheduled_on', 'placeholder': 'Scheduled On'}))

    def __init__(self, *args, **kwargs):
        super(AddCourtInfoForm, self).__init__(*args, **kwargs)
        self.fields['accused_person'].choices = [(e.pk, f"{e.first_name}" + ' ' + f"{e.middle_name}" + ' ' + f"{e.last_name}") for e in AccusedPerson.objects.all()]

    class Meta:
        model = Court
        fields = ['court_number', 'accused_person', 'court', 'court_verdict', 'scheduled_on']

class EditCourtInfoForm(forms.Form):
    court_number = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'court_number', 'class': 'form-control mb-4', 'name': 'court_number', 'placeholder': 'Court Number'}))
    accused_person = forms.ChoiceField(required=True, widget=forms.Select(attrs={'id': 'accused_person', 'class': 'form-control mb-4', 'name': 'accused_person', 'placeholder': 'Accused Person'}))
    court = forms.ChoiceField(choices=COURTS, required=True, widget=forms.Select(attrs={'id': 'court', 'class': 'form-control mb-4', 'name': 'court', 'placeholder': 'Court'}))
    court_verdict = forms.ChoiceField(choices=VERDICT, required=True, widget=forms.Select(attrs={'id': 'court_verdict', 'class': 'form-control mb-4', 'name': 'court_verdict', 'placeholder': 'Verdict'}))
    scheduled_on = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'id': 'scheduled_on', 'class': 'form-control mb-4', 'name': 'scheduled_on', 'placeholder': 'Scheduled On'}))

    def __init__(self, *args, **kwargs):
        super(EditCourtInfoForm, self).__init__(*args, **kwargs)
        self.fields['accused_person'].choices = [(e.pk, f"{e.first_name}" + ' ' + f"{e.middle_name}" + ' ' + f"{e.last_name}") for e in AccusedPerson.objects.all()]
    
    class Meta:
        model = Court
        fields = ['court_number', 'accused_person', 'court', 'court_verdict', 'scheduled_on']