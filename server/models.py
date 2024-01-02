from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import datetime

LEAGUE_CHOICES = (
    ('PL', 'Premier League'),
    ('LL', 'La Liga'),
    ('BL', 'BundesLiga'),
    ('SA', 'Serie A'),
    ('L1', 'Legue 1'),
    ('UCL', 'UEFA Champions League'),
    ('UEL', 'UEFA Europa League')
)

STATUS_CHOICES = (
    ('up', 'up'),
    ('down', 'down')
)


# Create your models here.
class User(AbstractUser):
    phone_number= models.CharField(max_length=50, blank=True, null=True)
    account_balance = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

class Fixture(models.Model):
    league = models.CharField(choices=LEAGUE_CHOICES, max_length=3,blank=True, null=True)
    home = models.CharField(max_length=50, blank=True, null=True)
    away = models.CharField(max_length=50, blank=True, null=True)
    home_score = models.CharField(max_length=50, blank=True, null=True)
    away_score = models.CharField(max_length=50, blank=True, null=True)
    home_image = models.ImageField(null=True,blank=True,upload_to = 'images/')
    away_image = models.ImageField(null=True,blank=True,upload_to = 'images/')
    home_win = models.CharField(max_length=50, blank=True, null=True)
    home_status = models.CharField(choices=STATUS_CHOICES, max_length=5,blank=True, null=True)
    draw = models.CharField(max_length=50, blank=True, null=True)
    draw_status = models.CharField(choices=STATUS_CHOICES, max_length=5,blank=True, null=True)
    away_win = models.CharField(max_length=50, blank=True, null=True)
    away_status = models.CharField(choices=STATUS_CHOICES, max_length=5,blank=True, null=True)
    in_play = models.BooleanField(default=False)
    date = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
   
    
    def __str__(self):
        return self.home
    
