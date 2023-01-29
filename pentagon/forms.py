from django.forms import ModelForm, DateInput, Textarea, NumberInput
from .models import Student
from captcha.fields import CaptchaField

class AdmissionForm(ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "first_name":"First Name", # Student Details
            "last_name":"Last Name",
            "dob":"Date of Birth",
            "nationality":"Nationality",
            "mother_tongue":"Mother Tongue",
            "grade":"Grade",
            "gender":"Gender",
            "religion":"Religion",
            "place_of_birth":"Place of Birth",
            "father_name":"Father's Name", # Parent Details
            "mother_name":"Mother's Name",
            "father_qualification":"Father's Qualification",
            "mother_qualification":"Mother's Qualification",
            "father_occupation":"Father's Occupation",
            "mother_occupation":"Mother's Occupation",
            "father_designation":"Father's Designation",
            "mother_designation":"Mother's Designation",
            "father_organisation":"Father's Organisation Name & Address",
            "mother_organisation":"Mother's Organisation Name & Address",
            "father_mobile":"Father's Mobile Number",
            "mother_mobile":"Mother's Mobile Number",
            "father_email":"Father's Email ID",
            "mother_email":"Mother's Email ID",
            "address":"Residential Address", # Residential Details
            "pincode":"Pincode"
        }
        widgets = {
        'dob': DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'address': Textarea(attrs={'cols': 20, 'rows': 3}),
        'father_mobile':NumberInput(),
        'mother_mobile':NumberInput(),
        'pincode':NumberInput(),
        }