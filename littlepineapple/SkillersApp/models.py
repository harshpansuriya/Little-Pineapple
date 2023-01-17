from django.db import models
from phone_field import PhoneField

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    contact_no = PhoneField()
    business_email = models.EmailField(blank=True)
    business_contact_no = PhoneField(blank=True)

    def __str__(self):
        return self.username

