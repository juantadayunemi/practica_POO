from django.db import models

# Create your models here.

SPECIALTY_CHOICES = [
    ('Cardiología', 'Cardiología'),
    ('Pediatría', 'Pediatría'),
    # Agrega más especialidades aquí
]

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, choices=SPECIALTY_CHOICES)
    honorarios = models.DecimalField(max_digits=7, decimal_places=2)  
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)  
