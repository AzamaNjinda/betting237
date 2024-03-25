# file created: 2024-02-06 22:43:14.883897

# this files has been generated by CandyTranslate.com  Please do not change manually
# author: Next Level Sense

# Available functions:
#    render - replacement for django render function
#    path - replacement for django path function. please use with * when replacing in urls.py
#    supported_languages - list that contains all available languages for this site
# Functions to be used in django templates:
#    languageReferences - create 'alternate' language references for SEO.
#        put it inside of the <head> section of the page in format {{languageReferences|safe}}
#    lang - current language. Used mostly in <html lang="{{lang}}">
#    languageMenu - adding language selection for your page. Format: {{languageMenu|safe}}
#    <<link variables>> - create linking to correct language link. 
#    usage:
#    for translated pages change {% url "my_page" %}
#    to name without quotes:     {% url my_page %}


supported_languages = ['en', 'fr']

def translation_dictionary(lang):
    if lang == 'en': return {
        'all_base_1':'''is loading''',
        'all_base_2':'''Deposit''',
        'all_base_3':'''create account''',
        'all_base_4':'''Home''',
        'all_base_5':'''about us''',
        'all_base_6':'''Football''',
        'all_base_7':'''Finished''',
        'all_base_8':'''Bet History''',
        'all_base_9':'''Balance:''',
        'all_base_10':'''Deposit''',
        'all_base_11':'''Withdrawal''',
        'all_base_12':'''Contact Us''',
        'all_base_13':'''Create Acount''',
        'all_base_14':'''Copyright © 2024. All Right Reserved By 1XBET RUSSIA''',
        'betslip_base_1':'''betslip''',
        'betslip_base_2':'''Your bet slip is empty!''',
        'betslip_base_3':'''looks like you haven’t placed''',
        'betslip_base_4':''' a bet yet to your bet slip.''',
        'betslip_base_5':'''Bet is placed successfully!''',
        'betslip_base_6':'''so, you can check your placed ''',
        'betslip_base_7':'''bets in dashboard.''',
        'betslip_base_8':'''overall odds:''',
        'betslip_base_9':'''Total stake:''',
        'betslip_base_10':'''Total est. return :''',
        'betslip_base_11':'''Place your bet ''',
        'index_index_1':'''Make place your bet online''',
        'index_index_2':'''BETTING ON THE GREAT SPORTS.''',
        'index_index_3':'''Bet Now''',
        'index_index_4':'''EXPLORE''',
        'index_index_5':'''Recent bet''',
        'index_index_6':'''Choose Your Match & Place A Bet''',
        'index_index_7':'''All Games''',
        'index_index_8':'''XXBET GAMES''',
        'index_index_9':'''Still Need Help or Confused to Placing A Bet?''',
        'index_index_10':'''Get Help ''',
        'index_index_11':'''How it works''',
        'index_index_12':'''Easiest Step To Placing A Bet''',
        'index_index_13':'''Open an  account.''',
        'index_index_14':'''Create an account. Enter your''',
        'index_index_15':'''personal details into the sign-up form & click the 'Register' button.''',
        'index_index_16':'''Make your deposit.''',
        'index_index_17':'''Before you can make to placing bet, you’ll need to deposit some cash in your account.''',
        'index_index_18':'''Place your wagers.''',
        'index_index_19':'''Now you’re ready to start placing''',
        'index_index_20':'''your bets online, so it’s time to make your selections.''',
        'index_index_21':'''Withdraw your winnings.''',
        'index_index_22':'''If you are a winner, claim your prize:''',
        'index_index_23':'''Be sure to visit a retailer before your prize expires in 12 months.''',
        'index_index_24':'''Reasonable odds''',
        'index_index_25':'''The odds offered in a Betting Exchange are relatively better than odds given by bookmakers.''',
        'index_index_26':'''Live Betting''',
        'index_index_27':'''live streaming allows you to watch the games you’re betting on, bringing you closer to the action.''',
        'index_index_28':'''Plenty of Options''',
        'index_index_29':'''we offer more than just betting options., Most of them allow you to stream games in real-time.''',
        'index_index_30':'''Easyest to Deposit''',
        'index_index_31':'''When you are looking to bet online you need to fund your account before you can place your bets.''',
        'index_index_32':'''Fastest Withdrawal''',
        'index_index_33':'''It's easy to get retrieve your balance at a fast withdrawal, and you won't be left waiting.''',
        'index_index_34':'''24/7 Friendly Support''',
        'index_index_35':'''Our customer care team are ready to deal with betting issues and are available to talk to you 24/7.''',
        'signup_signup_1':'''Create Account''',
        'signup_signup_2':'''Win with Us''',
        'signup_signup_3':'''Mobile Number''',
        'signup_signup_4':'''password''',
        'signup_signup_5':'''Re-enter password''',
        'login_login_1':'''Fill the form as well''',
        'login_login_2':'''No account yet in Peredion?''',
        'login_login_3':'''create account''',
        'login_login_4':'''here to signup.''',
        'login_login_5':'''or sign in with''',
        'login_login_6':'''Welcome to 1XBET RUSSIA''',
        'login_login_7':'''Sign in & Start Betting''',
        'login_login_8':'''with Just One Click''',
        'deposit_deposit_1':'''Deposit into Account''',
        'deposit_deposit_2':'''Enter Amount''',
        'deposit_deposit_3':'''Enter Phone Number''',
        'deposit_deposit_3_1':'''Enter Email''',
        'deposit_deposit_4':'''Select your payment wallet''',
        'nan_nan':'''We provide the most''',
        'nan_nan':'''reliable & legal betting''',
        }
    if lang == 'fr': return {
        'all_base_1':'''est en cours de chargement''',
        'all_base_2':'''Depot''',
        'all_base_3':'''creer un compte''',
        'all_base_4':'''Accueil''',
        'all_base_5':'''A propos de nous''',
        'all_base_6':'''Football''',
        'all_base_7':'''Fini''',
        'all_base_8':'''Historique des paris''',
        'all_base_9':'''L'equilibre :''',
        'all_base_10':'''Depot''',
        'all_base_11':'''Retrait''',
        'all_base_12':'''Nous contacter''',
        'all_base_13':'''Creer un compte''',
        'all_base_14':'''Copyright © 2024. Tous droits reserves par 1XBET RUSSIA''',
        'betslip_base_1':'''bulletin de mise''',
        'betslip_base_2':'''Votre bulletin de pari est vide''',
        'betslip_base_3':'''On dirait que vous n'avez pas misé''', 
        'betslip_base_4':''' 'Votre bulletin de pari est vide''', 
        'betslip_base_5':'''Le pari est placé avec succès!''',
        'betslip_base_6':'''alors, vous pouvez vérifier votre pari placé''',
        'betslip_base_7':'''bets in dashboard.''',
        'betslip_base_8':'''cote globale:''',
        'betslip_base_9':'''Mise totale:''',
        'betslip_base_10':'''Rendement total estimé:''',
        'betslip_base_11':'''Placez votre pari''',
        'index_index_1':'''Placez votre pari en ligne  ''',
        'index_index_2':'''LES PARIS SUR LES GRANDS SPORTS.''',
        'index_index_3':'''Parier maintenant''',
        'index_index_4':'''EXPLOREZ''',
        'index_index_5':'''Mise recente''',
        'index_index_6':'''Choisissez votre match et placez un pari''',
        'index_index_7':'''Toutes les ligues''',
        'index_index_8':'''Jeu classe''',
        'index_index_9':'''Vous avez encore besoin d'aide ou vous ne savez pas comment placer un pari ?''',
        'index_index_10':'''Obtenir de l'aide''',
        'index_index_11':'''Comment cela fonctionne-t-il ?''',
        'index_index_12':'''L'etape la plus simple pour placer un pari''',
        'index_index_13':'''Ouvrir un compte.''',
        'index_index_14':'''Creer un compte. Saisissez votre''',
        'index_index_15':'''dans le formulaire d'inscription et cliquez sur le bouton "S'inscrire".''',
        'index_index_16':'''Effectuez votre depot.''',
        'index_index_17':'''Avant de pouvoir placer un pari, vous devez deposer de l'argent sur votre compte.''',
        'index_index_18':'''Placez vos paris.''',
        'index_index_19':'''Vous etes maintenant pret a placer''',
        'index_index_20':'''vos paris en ligne, il est done temps de faire vos selections.''',
        'index_index_21':'''Retirez vos gains.''',
        'index_index_22':'''Si vous etes gagnant, reclamez votre prix :''',
        'index_index_23':'''N'oubliez pas de vous rendre chez un detaillant avant que votre prix n'expire dans 12 mois.''',
        'index_index_24':'''Des chances raisonnables''',
        'index_index_25':'''Les cotes proposees par les Betting Exchange sont relativement meilleures que celles des bookmakers.''',
        'index_index_26':''' Pari en direct''',
        'index_index_27':'''La diffusion en direct vous permet de regarder les matchs sur lesquels vous pariez, vous rapprochant ainsi de l'action.''',
        'index_index_28':'''De nombreuses options''',
        'index_index_29':'''La plupart d'entre eux vous permettent de regarder les matchs en temps reel.''',
        'index_index_30':'''Depot le plus facile''',
        'index_index_31':'''Lorsque vous souhaitez parier en ligne, vous devez approvisionner votre compte avant de pouvoir placer vos paris.''',
        'index_index_32':'''Retrait le plus rapide''',
        'index_index_33':'''Il est facile de recuperer votre solde en effectuant un retrait rapide, et vous ne resterez pas dans l' expectative.''',
        'index_index_34':'''Assistance amicale 24/7''',
        'index_index_35':'''Notre equipe d'assistance a la clientele est prete a traiter les questions relatives aux paris et est disponible pour vous parler 24 heures sur 24,''',
        'signup_signup_1':'''Creer un compte''',
        'signup_signup_2':'''Gagnez avec nous''',
        'signup_signup_3':'''Numero de telephone mobile''',
        'signup_signup_4':'''mot de passe''',
        'signup_signup_5':'''Reintroduire le mot de passe''',
        'login_login_1':'''Remplir egalement le formulaire''',
        'login_login_2':'''Pas encore de compte dans Peredion ?''',
        'login_login_3':'''creer un compte''',
        'login_login_4':'''ici pour s'inscrire.''',
        'login_login_5':'''ou se connecter avec''',
        'login_login_6':'''Bienvenue a 1XBET RUSSIA''',
        'login_login_7':'''S'inscrire et commencer a parier''',
        'login_login_8':'''en un seul clic''',
        'deposit_deposit_1':'''Déposer sur le compte''',
        'deposit_deposit_2':'''Entrez le montant''',
        'deposit_deposit_3':'''Entrez le numéro de téléphone''',
        'deposit_deposit_3_1':'''Entrez address Email''',
        'deposit_deposit_4':'''Sélectionnez votre portefeuille de paiement''',
        'nan_nan':'''A propos de nous''',
        'nan_nan':'''Nous fournissons le plus grand nombre de''',
        'nan_nan':'''des paris fiables et legaux''',
        }


def detectLanguage(request):
    languageDetected = supported_languages[0]
    pagePath = request.path
    if pagePath[-1] == '/': pagePath=pagePath[:-1]
    pagePath = pagePath.split('?')[0]
    pagePath = pagePath.split('#')[0]
    lastPath = pagePath.split('/')[-1]
    if lastPath in supported_languages[1:]:
        languageDetected = lastPath
    return languageDetected


def translated(requestOrLang,TranslateVariable):
    if requestOrLang in supported_languages:
        lang=requestOrLang
    else:
        lang = detectLanguage(requestOrLang)
    return translation_dictionary(lang)[TranslateVariable]


def localizeLink(request, link):
    lang=detectLanguage(request)
    if lang == supported_languages[0]: return link
    index1 = link.find('#')
    index2 = link.find('?')
    if index1 == -1 and index2 == -1: smallest_index = len(link)
    elif index1 == -1: smallest_index = index2
    elif index2 == -1: smallest_index = index1
    else: smallest_index = min(index1, index2)
    path = link[:smallest_index]
    if path[-1] == '/': path=path[:-1]
    return path+'/'+lang+link[smallest_index:]


from django.shortcuts import redirect as org_redirect
def redirect(request, to, *args, permanent=False, **kwargs):
    lang=detectLanguage(request)
    if lang in supported_languages[1:]:
        to=to+'_'+lang
    return org_redirect(to, *args, permanent=permanent, **kwargs)


from django.urls import path as org_path
def path(route, view, kwargs=None, name=None):
    if route == '':
        return [org_path('', view, kwargs, name),org_path('fr', view, kwargs, name+'_fr'),]
    if route[-1] == '/': route=route[:-1]
    return [org_path(route, view, kwargs, name),org_path(route+'/fr', view, kwargs, name+'_fr'),]


def langRef(path_ref):
    last=path_ref.split('/')[-1]
    if last in supported_languages:
        path_ref=path_ref[:-len(last)-1]
    result='<link rel="alternate" hreflang="en" href="'+addLinks(path_ref,'')+'" />\n'
    result+='<link rel="alternate" hreflang="fr" href="'+addLinks(path_ref,'fr')+'" />\n'
    result+='<link rel="alternate" hreflang="x-default" href="'+addLinks(path_ref,'')+'" />\n'
    return result


from django.urls import get_resolver
def translatedLinks(lang):
    names=[]
    for i in get_resolver().url_patterns:
        if hasattr(i, 'name'):
            if i.name:
                names.append(i.name)
    result = {}
    if lang == supported_languages[0]:
        for i in names:
            if i[-3:] not in ['_fr'] and names.count(i+'_fr'):
                result.update({i:i})
        return result
    for i in names:
        if names.count(i+'_'+lang):
            result.update({i:i+'_'+lang})
    return result


def languageMenu(request, lang):
    path = request.path
    remainder = request.get_full_path()[len(path):]
    selected = [' ', ' ']
    selected[supported_languages.index(lang)]=' selected '
    if supported_languages.index(lang):
        path=path[:-3]
    result = '<select id="languageMenu" onchange="window.location = this.value;">'
    if path == '/': path = ''
    if path =='':
        result += '<option'+selected[0]+'value="/'+remainder+'">English (English)</option>'
    else:
        result += '<option'+selected[0]+'value="' + path + remainder +'">English (English)</option>'
    result += '<option'+selected[1]+'value="' + path +'/fr'+remainder+'">French (Français)</option>'
    result += '</select>'
    return result


from django.shortcuts import render as org_render
def render(request, template_name, context=None, *args, **kwargs):
    lang=detectLanguage(request)
    if context == None:
        context={}
    return org_render(request, template_name, {**context,
                                                **translation_dictionary(lang),
                                                'lang':lang,
                                                'languageReferences':langRef(request.build_absolute_uri()),
                                                'languageMenu':languageMenu(request, lang),
                                                'candyLink':translatedLinks(lang),
                                                }, *args, **kwargs)


def addLinks(*args):
    result=''
    for i in args:
        if result and result[-1]=='/':result=result[:-1]
        if i and i[-1]=='/':i=i[:-1]
        if i and i[0]=='/':i=i[1:]
        if result and i: result+='/'
        result+=i
    return result


def provideSitemap(request, add_pages=[], remove_pages=[], remove_paths=[]):
    from django.http import HttpResponse
    result='<?xml version="1.0" encoding="UTF-8"?>'+'\n'
    result+='<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+'\n'
    domain= request.build_absolute_uri()
    domain=domain.split('/')[0]+'//'+domain.split('/')[2]+'/'
    paths = []
    for i in get_resolver().url_patterns:
        if str(type(i))=="<class 'django.urls.resolvers.URLPattern'>":
            try:
                route=i.pattern._route
                route=route.split('<')[0]
                if not route == 'sitemap.xml':
                    if 'robots.txt' not in route:
                        paths.append(addLinks(domain,route))
            except: pass
    paths+=add_pages
    paths=list(dict.fromkeys(paths))
    for route in paths:
        removed_path = False
        for removal in remove_paths:
            if route[:len(removal)] == removal: removed_path = True
        if not removed_path and route not in remove_pages:
            result+='<url>'+'\n'
            result+='<loc>'+route+'</loc>'+'\n'
            result+='</url>'+'\n'
    result+='</urlset>'
    result= result.encode('utf-8')
    return HttpResponse(result, content_type='application/xml; charset=utf-8')


def sitemap(add_pages=[], remove_pages=[], remove_paths=[]):
    return [org_path('sitemap.xml', provideSitemap,{'add_pages' :add_pages,'remove_pages': remove_pages, 'remove_paths': remove_paths})]


