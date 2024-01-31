from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'server'

urlpatterns = [
    path('', views.home, name='home'), 
    path('register/', views.register_view, name='register'), 
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'), 
    path('deposit/', views.deposit_view, name='deposit'), 
    path('withdraw/', views.withdraw, name='withdraw'), 
    path('about/', views.about, name='about'), 
    path('playing/', views.playing, name='playing'), 
    path('finished/', views.finished, name='finished'), 
    path('in_play/', views.in_play, name='in_play'), 
    path('upcoming/', views.upcoming, name='upcoming'), 
    path('contact/', views.contact, name='contact'), 
    path('payment_successful/', views.payment_successful, name='payment_successful'), 
    path('error/', views.error, name='error'), 
    path('place-bet/', views.place_bet, name='place-bet'), 
    path('bet-history/', views.bet_history, name='bet-history'), 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
