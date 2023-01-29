from cProfile import label
from django.db import models

grade_choices = [
    ('Nursery', 'Nur'),
    ('LKG', 'LKG'),
    ('UKG', 'UKG'),
    ('I', 'I'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('V', 'V'),
    ('VI', 'VI'),
    ('VII', 'VII'),
    ('VIII', 'VIII'),
    ('IX', 'IX'),
    ('X', 'X'),
    ('XI', 'XI'),
]

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class Student(models.Model):
    # Student Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    nationality = models.CharField(max_length=100)
    mother_tongue = models.CharField(max_length=100)
    grade = models.CharField(choices=grade_choices ,max_length=100)
    gender = models.CharField(choices=gender_choices ,max_length=100)
    religion = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=100)
    # Parent Details
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_qualification = models.CharField(max_length=100)
    mother_qualification = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    father_designation = models.CharField(max_length=100)
    mother_designation = models.CharField(max_length=100)
    father_organisation = models.CharField(max_length=150)
    mother_organisation = models.CharField(max_length=150)
    father_mobile = models.CharField(max_length=10)
    mother_mobile = models.CharField(max_length=10)
    father_email = models.EmailField(max_length=100)
    mother_email = models.EmailField(max_length=100)
    # Residential Details
    address = models.TextField()
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.first_name

        



