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

BET_STATUS_CHOICES = (
    ('Away Win', 'Away Win'),
    ('Home Win', 'Home Win'),
    ('Draw', 'Draw')
)


# Create your models here.
class User(AbstractUser):
    phone_number= models.CharField(max_length=50, blank=True, null=True)
    account_balance = models.IntegerField(default=0, blank=True, null=True)
    can_withdraw = models.BooleanField(default= False)

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
    

class BetHistory(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    stake_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    predicted_outcome = models.CharField( max_length=50,blank=True, null=True)
    actual_outcome = models.CharField( max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Bet on {self.fixture} with stake {self.stake_amount}"
    

class BetSlip(models.Model):
    slipID = models.CharField( max_length=50,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bet_histories = models.ManyToManyField(BetHistory, related_name='bet_slips')
    total_stake_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_payout = models.DecimalField(max_digits=10, decimal_places=2)
    is_winner = models.BooleanField(default=False)

    def __str__(self):
         return f"Betslip for {self.user}: Total Stake - {self.total_stake_amount}, Total Payout - {self.total_payout}"


class StakeAmount(models.Model):
    stake_amount_max = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"Global Stake amount {self.stake_amount_max }"
