# Generated by Django 4.2.7 on 2023-12-20 09:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import validations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='Email must end with@ur.ac.rw', regex='.*@ur.ac.rw$')])),
                ('phone_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator('^\\+(\\d{1,4})\\d{9}$', 'Enter a valid phone number starting with + country code and followed by 9 digits.')])),
                ('date_of_birth', models.DateField(validators=[validations.models.validate_age])),
                ('reference_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(99), django.core.validators.MaxValueValidator(999)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid plate number.', regex='^(RA[ABCDEFGH]|(RNP|RDF|GR|IT|CD))[0-9]{3}[0-9A-HJ-NP-Y]$')])),
                ('model', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=50)),
                ('manufacture_date', models.IntegerField(validators=[validations.models.Vehicle.validate_manufacture_date])),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='validations.participant')),
            ],
        ),
    ]
