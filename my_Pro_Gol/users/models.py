from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django import forms

# Create your models here.

VIDEO_FORMAT_CHOICES = [
    ('webm', 'WebM'),
    ('mpeg4', 'MPEG4'),
    ('mpeg2', 'MPEG-2'),
    ('mpegps', 'MPEGPS'),
    ('mov', 'MOV'),
    ('avi', 'AVI'),
    ('3gpp', '3GPP'),
    ('wmv', 'WMV'),
    ('flv', 'FLV'),
]

class DateInput(forms.DateInput):
    input_type = 'date'

class Person(models.Model): #tabla
    name = models.CharField(max_length=50) #columnas
    last_name = models.CharField(max_length=50)
    regd_date = models.DateTimeField(null=True)


class Videos(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=50)
    extension = models.CharField(max_length=8, choices=VIDEO_FORMAT_CHOICES)
    size = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.1), MaxValueValidator(3.0)]
    )


class SignUp(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name", "last_name", "regd_date"]
        widgets = {
            'regd_date': DateInput(),  #calendario
        }


class Upload(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ["title", "extension", "size"]