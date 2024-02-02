from django.shortcuts import render, redirect, get_object_or_404
from server.forms import UserRegisterForm, UserLoginForm, PaymentForm, WithdrawalForm, ContactForm
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib import messages
import requests
import asyncio
import aiohttp
import uuid
from . models import Fixture
from django.db import transaction
from random import randint
from django.core.cache import cache
from asgiref.sync import sync_to_async
from django.db.models import Q  # Import Q for complex queries
from pymesomb.operations import PaymentOperation
from pymesomb.utils import RandomGenerator
from datetime import datetime
from django.contrib.auth.decorators import login_required
from . models import BetHistory, BetSlip, StakeAmount
from django.db.models import Case, When, Value, F, IntegerField


async def fetch_data(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            return await response.json()

async def fetch_all_data(urls_and_params):
    tasks = [fetch_data(url, params) for url, params in urls_and_params]
    return await asyncio.gather(*tasks)



def home(request):
    user = request.user
    fixtures =  Fixture.objects.all()
    fixture_Premiere_League = Fixture.objects.filter(league="PL",is_finished=False)
    fixture_La_Liga = Fixture.objects.filter(league="LL",is_finished=False)
    fixture_Bundesliga = Fixture.objects.filter(league="BL",is_finished=False)
    fixture_SerieA = Fixture.objects.filter(league="SA",is_finished=False)
    fixture_Ligue_1= Fixture.objects.filter(league="L1",is_finished=False)
    fixture_UEFA_Champions_League = Fixture.objects.filter(league="UCL",is_finished=False)
    fixture_UEFA_Europa_League = Fixture.objects.filter(league="UEL",is_finished=False)
    fixture_Classified_Game = Fixture.objects.filter(league="CLG",is_finished=False)

    max_stake_amount = StakeAmount.objects.first()

    # base_url = "https://api-football-v1.p.rapidapi.com/v3"

    # leagues = [
    #     {"name": "Premier League", "code": "GB", "league_id": "39"},
    #     {"name": "La Liga", "code": "ES", "league_id": "140"},
    #     {"name": "Bundesliga", "code": "DE", "league_id": "78"},
    #     {"name": "Serie A", "code": "IT", "league_id": "135"},
    #     {"name": "Ligue 1", "code": "FR", "league_id": "61"},
    #     {"name": "UEFA Champions League", "league_id": "2"},
    #     {"name": "UEFA Europa League", "league_id": "3"},
    # ]

    # headers = {
    #     "X-RapidAPI-Key": "bf5f2223fdmsh6b059a6898e8c6dp1b2f96jsn1d9956c224b2",
    #     "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    # }

    odds_data = []
    fixtures_data = []

    # league_ids = [league["league_id"] for league in leagues]
    # odds_querystring = {"league": ",".join(league_ids), "season": "2023"}

    # # Check cache first
    # cache_key = f"odds_data_{','.join(league_ids)}"
    # cached_response = cache.get(cache_key)

    # if not cached_response:
    #     response_odd = requests.get(f"{base_url}/odds", headers=headers, params=odds_querystring).json()
    #     cache.set(cache_key, response_odd, timeout=60 * 5)  # Cache for 5 minutes
    # else:
    #     response_odd = cached_response

    # if "response" in response_odd:
    #     fixtures_odds_data = extract_fixtures_odds_data(response_odd["response"])
    #     odds_data.extend(fixtures_odds_data)

    # fixture_ids = [odds_entry['fixture_id'] for odds_entry in odds_data]

    # # Batch database queries
    # # fixtures = YourFixtureModel.objects.filter(id__in=fixture_ids)
    # # fixtures_data.extend(extract_fixtures_data(fixtures))

    # # Fetch fixture details using asynchronous requests
    # urls_and_params = [(f"{base_url}/fixtures", {"id": fixture_id}) for fixture_id in fixture_ids]
    # task = asyncio.create_task(fetch_all_data(urls_and_params))
    # response_fixture_details = await task
    # #response_fixture_details = asyncio.run(fetch_all_data(urls_and_params))

    # for fixture_details_data in response_fixture_details:
    #     if "response" in fixture_details_data:
    #         fixture_details = extract_fixture_details(fixture_details_data["response"])
    #         fixtures_data.append(fixture_details)
    # print(fixtures_data)
    context = {
        'name': 'index',
        'class': 'active',
        'fixtures': fixtures,
        'odds_data': odds_data,
        'fixtures_data': fixtures_data,
        'fixture_Premiere_League': fixture_Premiere_League,
        'fixture_La_Liga':fixture_La_Liga,
        'fixture_Bundesliga':fixture_Bundesliga,
        'fixture_SerieA':fixture_SerieA,
        'fixture_Ligue_1':fixture_Ligue_1,
        'fixture_UEFA_Champions_League':fixture_UEFA_Champions_League,
        'fixture_UEFA_Europa_League':fixture_UEFA_Europa_League,
        'max_stake_amount': max_stake_amount.stake_amount_max, 
        'fixture_Classified_Game':fixture_Classified_Game

    }

    return render(request, "index.html", context)




def login_view(request):
    next = request.GET.get('server:home')
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            phoneNumber = form.cleaned_data.get('phoneNumber')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=phoneNumber, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('server:home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    context = {
        'form': form,
    }
    return render(request, "sign-in.html", context)

def extract_fixtures_odds_data(response_odd):
    fixtures_odds_data = []

    for fixture_data in response_odd:
        if 'bookmakers' in fixture_data and fixture_data['bookmakers']:
            fixtures_odds_data.append({
                'fixture_id': fixture_data['fixture']['id'],
                'home_odds': next((value['odd'] for bet in fixture_data['bookmakers'][0]['bets'] if bet['name'] == 'Match Winner' for value in bet['values'] if value['value'] == 'Home'), None),
                'draw_odds': next((value['odd'] for bet in fixture_data['bookmakers'][0]['bets'] if bet['name'] == 'Match Winner' for value in bet['values'] if value['value'] == 'Draw'), None),
                'away_odds': next((value['odd'] for bet in fixture_data['bookmakers'][0]['bets'] if bet['name'] == 'Match Winner' for value in bet['values'] if value['value'] == 'Away'), None),
            })

    return fixtures_odds_data


def extract_fixtures_data(response_fixture):
    fixtures_data = []

    for fixture_data in response_fixture:
        fixture = fixture_data['fixture']
        league = fixture_data['league']
        teams = fixture_data['teams']
        score = fixture_data['score']['fulltime']

        fixture_info = {
            'fixture_id': fixture['id'],
            'league_name': league['name'],
            'home_team': teams['home']['name'],
            'away_team': teams['away']['name'],
            'full_time_score_home': score['home'],
            'full_time_score_away': score['away'],
        }

        fixtures_data.append(fixture_info)

    return fixtures_data

def extract_fixture_details(response_fixture_details):
    fixture_details_data = response_fixture_details[0]  # Assuming the response is a list with a single element
    fixture = fixture_details_data['fixture']
    league = fixture_details_data['league']
    teams = fixture_details_data['teams']
    score = fixture_details_data['score']['fulltime']

    fixture_details = {
        'fixture_id': fixture['id'],
        'league_name': league['name'],
        'home_team': teams['home']['name'],
        'away_team': teams['away']['name'],
        'full_time_score_home': score['home'],
        'full_time_score_away': score['away'],
    }

    return fixture_details

def register_view(request):
    home = request.GET.get('server:home')
    form = UserRegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            phoneNumber = form.cleaned_data.get('phoneNumber')
            user.set_password(password)
            user.phone_number = phoneNumber
            user.username = phoneNumber
            user.save()

            new_user = authenticate(request, username=phoneNumber, password=password)
            login(request, new_user)

            if home:
                return redirect("server:home")
            else:
                return redirect("server:home")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    # If the form is not valid or it's a GET request, render the registration form.
    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
@transaction.atomic
def deposit_view(request):
    home = request.GET.get('server:home')
    form = PaymentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            phoneNumber = form.cleaned_data.get('phoneNumber')
        # print(phoneNumber)
            amount = form.cleaned_data.get('amount')
            payment_method = form.cleaned_data.get('payment_method')
            #nonce = randint(100000, 999999)
            
            return redirect("https://hter.link/FNnzL")
            
    #         trxID = str(uuid.uuid4())
    #         operation = PaymentOperation('3b08794ed8f9a0c68eb16b324bc06920e96d6b04', 'd61ad5f4-cbfa-4e06-91c2-ccd1471e4a55', '56ef9d32-9919-414e-a631-7b41ab3784b0')
    #         try:
    #             response = operation.make_collect({
    #                 'amount': amount,
    #                 'service': payment_method,
    #                 'payer': phoneNumber,
    #                 'date': datetime.now(),
    #                 'nonce': nonce ,#RandomGenerator.nonce(),
    #                 'trxID': trxID
    #             })
    #             if response.is_operation_success() is True:
    #                 user.account_balance = user.account_balance + amount
    #                 user.save()
    #                 return redirect("server:payment_successful")
    #             else:
    #                 context = {
    #                 'message': "ERROR : Payment Not Successf ",
    #                 'form': form,
    #             }
    #         except Exception as e:
    #             print(f"MeSomb API error: {e}")
    #             context = {
    #                 'message': "Payment Not Successful, Try again",
    #                 'form': form,
    #             }
    #         return render(request, "dashboard-deposit.html", context)

    #     else:
    #         context = {
    #             'message': form.errors,
    #             'form': form,
    #         }
    #         return render(request, "dashboard-deposit.html", context)

    
    context = {
        'form': form,
    }

    return render(request, "dashboard-deposit.html", context )

@login_required(login_url='/login/')
def withdraw(request):
    bet_success = request.GET.get('server:payment_successful')
    form = WithdrawalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            phoneNumber = form.cleaned_data.get('phoneNumber')
            trxID = str(uuid.uuid4())
        # print(phoneNumber)
            amount = form.cleaned_data.get('amount')
            payment_method = form.cleaned_data.get('payment_method')
            if user.account_balance < amount:
                context = {
                    'message': "You do Not have Enough Funds to Withdraw",
                    'form': form,
                }
                return render(request, "dashboard-withdraw.html", context)
            elif user.can_withdraw is False:
                context = {
                    'message': "You Can Not Withdraw Funds at this tie",
                    'form': form,
                }
                return render(request, "dashboard-withdraw.html", context)


            operation = PaymentOperation('3b08794ed8f9a0c68eb16b324bc06920e96d6b04', 'd61ad5f4-cbfa-4e06-91c2-ccd1471e4a55', '56ef9d32-9919-414e-a631-7b41ab3784b0')
            try:
                response = operation.make_deposit({
                    'amount': amount,
                    'service': payment_method,
                    'receiver': phoneNumber,
                    'date': datetime.now(),
                    'nonce': RandomGenerator.nonce(),
                    'trxID': trxID
                })
                if response.is_operation_success() is True:
                    user.account_balance = user.account_balance - amount
                    user.save()
                    return redirect("server:home")
                else:
                    context = {
                    'message': "Withdrawal Not Successful",
                    'form': form,
                }
                return render(request, "dashboard-withdraw.html", context)
            except Exception as e:
                print(f"MeSomb API error: {e}")
                context = {
                    'message': "Withdrawal Not Successful",
                    'form': form,
                }
        else:
            context = {
                'message': form.errors,
                'form': form,
            }
            return render(request, "dashboard-withdraw.html", context)

    
    context = {
        'form': form,
    }

    return render(request, "dashboard-withdraw.html", context)

@login_required(login_url='/login/')
def place_bet(request):
    user = request.user
    if request.method == 'POST':
        # Retrieve data from the POST request
        slip_id = request.POST.get('slipID')
        fixture_id = request.POST.get('fixture')
        stake_amount = request.POST.get('stake_amount')
        predicted_outcome = request.POST.get('predicted_outcome')
        total_stake_amount = request.POST.get('total_stake_amount')
        total_payout = request.POST.get('total_payout')

        fixture = get_object_or_404(Fixture, id=fixture_id)

        print("Hello" + total_stake_amount )
        
    
        bet_slip_query = BetSlip.objects.filter(slipID=slip_id)
        
        if bet_slip_query.exists():
            bet_slip = bet_slip_query.first()
            bet_slip.is_combo = True
            bet_slip.save()
        else:
            bet_slip = BetSlip.objects.create(slipID=slip_id, user=user, total_stake_amount=float(total_stake_amount), total_payout=float(total_payout))

        bet_history = BetHistory.objects.create(fixture=fixture, stake_amount=float(stake_amount), predicted_outcome=predicted_outcome)
        bet_slip.bet_histories.set([bet_history])
                
        user.account_balance  = user.account_balance - int(total_stake_amount)
        
        if user.account_balance < 0:
            user.account_balance = 0

        user.save()

        
        data = {'message': f'Hello from Django! You entered: { slip_id,fixture_id,stake_amount,predicted_outcome,total_stake_amount,total_payout}'}

        return JsonResponse(data)
    else:
        # If the request is not a POST request, return an error response
        return JsonResponse({'error': 'Invalid request method'})

def about(request):
    return render(request, "about.html")

def playing(request):
    user = request.user
    fixtures =  Fixture.objects.all()
    fixture_Premiere_League = Fixture.objects.filter(league="PL",is_finished=False)
    fixture_La_Liga = Fixture.objects.filter(league="LL",is_finished=False)
    fixture_Bundesliga = Fixture.objects.filter(league="BL",is_finished=False)
    fixture_SerieA = Fixture.objects.filter(league="SA",is_finished=False)
    fixture_Ligue_1= Fixture.objects.filter(league="L1",is_finished=False)
    fixture_UEFA_Champions_League = Fixture.objects.filter(league="UCL",is_finished=False)
    fixture_UEFA_Europa_League = Fixture.objects.filter(league="UEL",is_finished=False)
    fixture_Classified_Game = Fixture.objects.filter(league="CLG",is_finished=False)

    max_stake_amount = StakeAmount.objects.first()
    odds_data = []
    fixtures_data = []


    context = {
        'name': 'index',
        'class': 'active',
        'fixtures': fixtures,
        'fixtures_data': fixtures_data,
        'fixture_Premiere_League': fixture_Premiere_League,
        'fixture_La_Liga':fixture_La_Liga,
        'fixture_Bundesliga':fixture_Bundesliga,
        'fixture_SerieA':fixture_SerieA,
        'fixture_Ligue_1':fixture_Ligue_1,
        'fixture_UEFA_Champions_League':fixture_UEFA_Champions_League,
        'fixture_UEFA_Europa_League':fixture_UEFA_Europa_League,
        'max_stake_amount': max_stake_amount.stake_amount_max, 
        'fixture_Classified_Game':fixture_Classified_Game

    }
    return render(request, "playing-bet.html", context)

def in_play(request):
    return render(request, "playing-bet-in-play.html")

def finished(request):
    user = request.user
    fixtures =  Fixture.objects.all()
    #fixture_is_finished = Fixture.objects.filter(is_finished=True)
    fixture_Premiere_League = Fixture.objects.filter(league="PL",is_finished=True)
    fixture_La_Liga = Fixture.objects.filter(league="LL",is_finished=True)
    fixture_Bundesliga = Fixture.objects.filter(league="BL",is_finished=True)
    fixture_SerieA = Fixture.objects.filter(league="SA",is_finished=True)
    fixture_Ligue_1= Fixture.objects.filter(league="L1",is_finished=True)
    fixture_UEFA_Champions_League = Fixture.objects.filter(league="UCL",is_finished=True)
    fixture_UEFA_Europa_League = Fixture.objects.filter(league="UEL",is_finished=True)
    fixture_Classified_Game = Fixture.objects.filter(league="CLG",is_finished=True)

    max_stake_amount = StakeAmount.objects.first()
    odds_data = []
    fixtures_data = []


    context = {
        'name': 'index',
        'class': 'active',
        'fixtures': fixtures,
        'fixtures_data': fixtures_data,
        'fixture_Premiere_League': fixture_Premiere_League,
        'fixture_La_Liga':fixture_La_Liga,
        'fixture_Bundesliga':fixture_Bundesliga,
        'fixture_SerieA':fixture_SerieA,
        'fixture_Ligue_1':fixture_Ligue_1,
        'fixture_UEFA_Champions_League':fixture_UEFA_Champions_League,
        'fixture_UEFA_Europa_League':fixture_UEFA_Europa_League,
        'max_stake_amount': max_stake_amount.stake_amount_max, 
        'fixture_Classified_Game':fixture_Classified_Game

    }
    return render(request, "playing-bet-finished.html", context)

def upcoming(request):
    return render(request, "playing-bet-upcoming.html")

def contact(request):
    home = request.GET.get('server:home')
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save(commit=False)
            context = {
                'message':'Message Successfully Sent',
                'form': form,
                }
            return render(request, "contact.html", context)
            

    context = {
        'form': form,
    }
    return render(request, "contact.html", context)

@login_required(login_url='/login/')
def payment_successful(request):
    # user = request.user
    # user.account_balance = user.account_balance + amount
    # user.save()
    return render(request, "payment-successful.html")

def bet_history(request):
    user = request.user
    bet_slips = BetSlip.objects.filter(user=request.user).order_by('-created_at')
    bet_slips_data = []
    bet_histories = []
    fixtures = []
    for bet_slip in bet_slips:
        bet_histories = bet_slip.bet_histories.select_related('fixture')
        fixtures = [bet_history.fixture for bet_history in bet_histories]
        #bet_slip.is_winner = True

        for bet_history in bet_histories:
            fixture = bet_history.fixture
            if fixture.is_finished:
                if fixture.home_score > fixture.away_score:
                    bet_history.actual_outcome = "Home Win"
                    bet_slip.is_winner = True
                elif fixture.home_score == fixture.away_score:
                    bet_history.actual_outcome = "Draw"
                    bet_slip.is_winner = True
                else:
                    bet_history.actual_outcome = "Away Win"
                    bet_slip.is_winner = True

                bet_history.save()

                if bet_history.predicted_outcome != bet_history.actual_outcome:
                    bet_slip.is_winner = False

        if bet_slip.is_winner and not bet_slip.is_paid:
            user.account_balance += bet_slip.total_payout
            bet_slip.is_paid = True
            bet_slip.save()
            user.save()
            # if fixture.is_finished is True:
            #     if fixture.home_score > fixture.away_score:
            #         bet_history.actual_outcome = "Home Win"
            #         bet_history.save()
            #         if bet_history.predicted_outcome == bet_history.actual_outcome:
            #             bet_slip.is_winner = True
            #             bet_slip.save()
            #             if not bet_slip.is_paid:
            #                 user.account_balance = user.account_balance + bet_slip.total_payout
            #                 bet_slip.is_paid = True
            #                 bet_slip.save()
            #                 user.save()
            #             else:
            #                 pass
            #         else:
            #             bet_slip.is_winner = False
            #             bet_slip.save()
            #     elif fixture.home_score == fixture.away_score:
            #         bet_history.actual_outcome = "Draw"
            #         bet_history.save()
            #         if bet_history.predicted_outcome == bet_history.actual_outcome:
            #             bet_slip.is_winner = True
            #             bet_slip.save()
            #             if not bet_slip.is_paid:
            #                 user.account_balance = user.account_balance + bet_slip.total_payout
            #                 bet_slip.is_paid = True
            #                 bet_slip.save()
            #                 user.save()
            #             else:
            #                 pass
            #         else:
            #             bet_slip.is_winner = False
            #             bet_slip.save()
            #     elif fixture.home_score < fixture.away_score:
            #         bet_history.actual_outcome = "Away Win"
            #         bet_history.save()
            #         if bet_history.predicted_outcome == bet_history.actual_outcome:
            #             bet_slip.is_winner = True
            #             bet_slip.save()
            #             if not bet_slip.is_paid:
            #                 user.account_balance = user.account_balance + bet_slip.total_payout
            #                 bet_slip.is_paid = True
            #                 bet_slip.save()
            #                 user.save()
            #             else:
            #                 pass
            #         else:
            #             bet_slip.is_winner = False
            #             bet_slip.save()

        bet_slip_data = {
            'bet_slip': bet_slip,
            'bet_histories': bet_histories,
            'fixtures': fixtures,
        }

        bet_slips_data.append(bet_slip_data)        
       

         
    
    context = {
        'bet_slips': bet_slips,
        'bet_histories': bet_histories,
        'fixtures' : fixtures,
        'bet_slips_data': bet_slips_data,
    }

    return render(request, "dashboard-bet-history.html", context)

  
def error(request):
    context = {
        'title': "Inadequate Balance",
        'message': "Your Account Balance is not Sufficient to Place this Bet, Please Deposit into Account",
        }
    return render(request, "error.html", context)

