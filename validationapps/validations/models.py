from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,RegexValidator, EmailValidator
from datetime import date

from jsonschema import ValidationError

def validate_age(value):
    if value.year > date.today().year - 18:
        raise ValidationError('Participants must be 18 years old or above.', code = 'Invalid')
            
        
        
        date_of_birth = models.DateField(validators=[validate_age])

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[RegexValidator(regex=r'.*@ur.ac.rw$', message='Email must end with@ur.ac.rw')])
    phone_number = models.CharField(max_length=15, unique=True, validators=[RegexValidator(r'^\+(\d{1,4})\d{9}$', 'Enter a valid phone number starting with + country code and followed by 9 digits.')])
    date_of_birth = models.DateField(validators=[validate_age])
    reference_number = models.IntegerField(validators=[MinValueValidator(99), MaxValueValidator(999)])
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
   


class Vehicle(models.Model): 
    def validate_manufacture_date(value):
        current_year=date.today().year
        if value <2000 or value > current_year:
            raise ValidationError('manufacture date should be between 2000 and the current year,')

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='vehicles')
    plate_number_validator = RegexValidator(
        regex=r'^(RA[ABCDEFGH]|(RNP|RDF|GR|IT|CD))[0-9]{3}[0-9A-HJ-NP-Y]$', 
        message='Enter a valid plate number.'
    )

    plate_number = models.CharField(
        max_length=20, 
        validators=[plate_number_validator],
        unique=True
    )

    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    colour = models.CharField(max_length=50)
    manufacture_date = models.IntegerField(validators=[validate_manufacture_date])
    #participant = models.ForeignKey(participant, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return f"{self.plate_number} - {self.model}"
    
    