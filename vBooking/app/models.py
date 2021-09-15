from django.db import models
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    content = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return f'{self.title} - {self.date}'

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    date = models.CharField(max_length=20, blank=False)
    time = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f'{self.name} ({self.date} {self.time})'

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    event= models.ForeignKey(Event, on_delete=models.CASCADE, blank=False)
    email = models.EmailField(blank=False)
    surname = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=30, blank=False)
    zipcode = models.CharField(max_length=6, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    proof = models.CharField(choices=[('tested', 'Getestet'), ('vaccinated', 'Geimpft'), ('recovered', 'Genesen')], max_length=10, blank=False, default=None)
    entry = models.CharField(choices=[('paid', 'Bezahlt'), ('vip', 'Gästeliste')], max_length=4, blank=True, default=None)

    def __str__(self):
        return f'{self.surname} {self.name} @ {self.event.name}'
