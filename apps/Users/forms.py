from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from apps.Users.models import Profile

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

ROLES = [
    ("Police Officer", "Police Officer"),
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

GENDER = [
    ('Male', ('Male')),
    ('Female', ('Female')),
]

class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'Old Password',}))
    new_password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'New Password',}))
    new_password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'Confirm Password',}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2',)

def clean_old_password(self):
    old_password = self.cleaned_data["old_password"]
    if not self.user.check_password(old_password):
        raise forms.ValidationError(
            self.error_messages['password_incorrect'],
            code='password_incorrect',
        )
    return old_password

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'readonly':'readonly'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'readonly':'readonly'}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'readonly':'readonly'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'readonly':'readonly'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(forms.ModelForm):
    middle_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Middle Name', 'readonly':'readonly'}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'dropify', 'data-height':420, 'data-max-file-size':"1M"}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control mb-4', 'style': "height: 150px", 'placeholder':'Keep it short, preferably in one concise sentence'}))
    national_id = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'National ID', 'readonly':'readonly'}))
    date_of_birth = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder':'Date Of Birth', 'readonly':'readonly'}))
    police_station = forms.ChoiceField(choices=STATIONS, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4'}))
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4', 'readonly':'readonly'}))
    role = forms.ChoiceField(choices=ROLES, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4'}))
    county = forms.ChoiceField(choices=COUNTIES, required=True, widget=forms.Select(attrs={'class': 'form-control mb-4'}))

    class Meta:
        model = Profile
        fields = ['middle_name', 'profile_picture', 'bio', 'national_id', 'date_of_birth', 'police_station', 'gender', 'role', 'county']