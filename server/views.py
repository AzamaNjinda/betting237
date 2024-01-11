from django.shortcuts import render, redirect
from server.forms import UserRegisterForm, UserLoginForm, PaymentForm, WithdrawalForm
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
import requests
import asyncio
import aiohttp
from . models import Fixture
from django.core.cache import cache
from asgiref.sync import sync_to_async
from django.db.models import Q  # Import Q for complex queries
from pymesomb.operations import PaymentOperation
from pymesomb.utils import RandomGenerator
from datetime import datetime


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
    fixture_Premiere_League = Fixture.objects.filter(league="PL")
    fixture_La_Liga = Fixture.objects.filter(league="LL")
    fixture_Bundesliga = Fixture.objects.filter(league="BL")
    fixture_SerieA = Fixture.objects.filter(league="SA")
    fixture_Ligue_1= Fixture.objects.filter(league="L1")
    fixture_UEFA_Champions_League = Fixture.objects.filter(league="UCL")
    fixture_UEFA_Europa_League = Fixture.objects.filter(league="UEL")
    

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
        'fixture_UEFA_Europa_League':fixture_UEFA_Europa_League 

    }

    return render(request, "index.html", context)




def login_view(request):
    next = request.GET.get('server:home')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        phoneNumber = form.cleaned_data.get('phoneNumber')
        password = form.cleaned_data.get('password')
        user = authenticate(phone_number=phoneNumber, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('server:home')
    else:
        print(form.errors)
        context = {
            'message': form.errors,
            'form': form,
        }
        return render(request, "sign-in.html", context)

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
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        phoneNumber = form.cleaned_data.get('phoneNumber')
        user.set_password(password)
        user.phone_number = phoneNumber
        user.save()
        new_user = authenticate(phoneNumber=user.phone_number, password=password)
        login(request, new_user)
        if home:
            return redirect("server:home")
        return redirect("server:home")
    else:
        print(form.errors)
        context = {
            'message': form.errors,
            'form': form,
        }
        return render(request, "signup.html", context)

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

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
            operation = PaymentOperation('aee1c21026333a7eb9712c18a83ad5217aab77e3', 'a52b21e9-640c-477f-ae3a-6b744273d868', 'a785efe3-85e7-4923-85c1-dbdd3eae4764')
            response = operation.make_collect({
                'amount': amount,
                'service': payment_method,
                'payer': phoneNumber,
                'date': datetime.now(),
                'nonce': RandomGenerator.nonce(),
                'trxID': '1'
            })
            if response.is_operation_success() is True:
                user.account_balance = user.account_balance + amount
                user.save()
                return redirect("server:home")
            else:
                context = {
                'message': "Payment Not Successful",
                'form': form,
            }
            return render(request, "dashboard/dashboard-deposit.html", context)

            
            if home:
                return redirect("server:home")
            return redirect("server:home")
        else:
            context = {
                'message': form.errors,
                'form': form,
            }
            return render(request, "dashboard/dashboard-deposit.html", context)

    
    context = {
        'form': form,
    }

    return render(request, "dashboard/dashboard-deposit.html", context )

def withdraw(request):
    home = request.GET.get('server:home')
    form = WithdrawalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            phoneNumber = form.cleaned_data.get('phoneNumber')
        # print(phoneNumber)
            amount = form.cleaned_data.get('amount')
            payment_method = form.cleaned_data.get('payment_method')
            operation = PaymentOperation('aee1c21026333a7eb9712c18a83ad5217aab77e3', 'a52b21e9-640c-477f-ae3a-6b744273d868', 'a785efe3-85e7-4923-85c1-dbdd3eae4764')
            response = operation.make_deposit({
                'amount': amount,
                'service': payment_method,
                'payer': phoneNumber,
                'date': datetime.now(),
                'nonce': RandomGenerator.nonce(),
                'trxID': '1'
            })
            if response.is_operation_success() is True:
                user.account_balance = user.account_balance - amount
                user.save()
                return redirect("server:home")
            else:
                context = {
                'message': "Payment Not Successful",
                'form': form,
            }
            return render(request, "dashboard/dashboard-withdraw.html", context)

            
            if home:
                return redirect("server:home")
            return redirect("server:home")
        else:
            context = {
                'message': form.errors,
                'form': form,
            }
            return render(request, "dashboard/dashboard-withdraw.html", context)

    
    context = {
        'form': form,
    }

    return render(request, "dashboard/dashboard-withdraw.html", context)

def about(request):
    return render(request, "about.html")

def playing(request):
    return render(request, "playing-bet.html")

def in_play(request):
    return render(request, "playing-bet-in-play.html")

def upcoming(request):
    return render(request, "playing-bet-upcoming.html")

def contact(request):
    return render(request, "contact.html")



