from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from server import candy

app_name = 'server'

urlpatterns = [
    *candy.path('', views.home, name='home'), 
    *candy.path('register/', views.register_view, name='register'), 
    *candy.path('login/', views.login_view, name='login'), 
    *candy.path('logout/', views.logout_view, name='logout'), 
    *candy.path('deposit/', views.deposit_view, name='deposit'), 
    *candy.path('withdraw/', views.withdraw, name='withdraw'), 
    *candy.path('about/', views.about, name='about'), 
    *candy.path('playing/', views.playing, name='playing'), 
    *candy.path('finished/', views.finished, name='finished'), 
    *candy.path('in_play/', views.in_play, name='in_play'), 
    *candy.path('upcoming/', views.upcoming, name='upcoming'), 
    *candy.path('contact/', views.contact, name='contact'), 
    path('payment_successful/', views.payment_successful, name='payment_successful'), 
    path('error/', views.error, name='error'), 
    path('error2/', views.error_2, name='error2'), 
    path('error3/', views.error_3, name='error3'), 
    path('error4/', views.error_4, name='error4'), 
    path('error5/<stakelimit>', views.error_5, name='error5'),
    path('place-bet/', views.place_bet, name='place-bet'), 
    *candy.path('bet-history/', views.bet_history, name='bet-history'), 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
