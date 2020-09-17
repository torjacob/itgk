#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving1.ipynb">Øving 1</a>
#     </div>
#     <ul class="nav navbar-nav">
#         <li><a href="Intro%20til%20jupyter.ipynb">Intro til Jupyter</a></li>
#       <li ><a href="Jeg%20elsker%20ITGK!.ipynb">Jeg elsker ITGK!</a></li>
#     <li ><a href="Kalkulasjoner.ipynb">Kalkulasjoner</a></li>
#     <li><a href="Input%20og%20variable.ipynb">Input og variable</a></li>
#     <li><a href="Tallkonvertering.ipynb">Tallkonvertering</a></li>
#     <li ><a href="Peppes%20Pizza.ipynb">Peppes Pizza</a></li>
#     <li ><a href="Geometri.ipynb">Geometri</a></li>
#     <li ><a href="Vitenskapelig%20notasjon.ipynb">Vitenskapelig notasjon</a></li>
#     <li ><a href="Tetraeder.ipynb">Tetraeder</a></li>
#     <li ><a href="Bakekurs.ipynb">Bakekurs</a></li>
#     <li class="active"><a href="James%20Bond%20and%20Operation%20round().ipynb">James Bond and Operation Round</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # James Bond and Operation round()
# 
# **Læringsmål:**
# 
# * Bruk av heltallsdivisjon og modulo, konvertering av data
# 
# * Avrunding
# * (særlig c) Oppdeling / håndtering av strenger
# 
# **Starting Out with Python:**
# 
# * Kap. 2.3
# 
# * Kap. 3.1
# 
# * Kap. 4.2
# 
# * Kap. 8.2

# ## a) Kjøpmannsavrunding

# "Kjøpmannsavrunding" innebærer at man alltid runder opp når et tall er midt mellom to runde tall. F.eks. at 2.5 rundes til 3 og 3.5 til 4 hvis vi skal ha hele tall, og 2.25 likeledes rundes til 2.3 hvis vi skal ha en desimal. Som forklart i tutorial i oppgaven Tallkonvertering (tidligere i denne samme øvingen) bruker Pythons funksjon `round()` **ikke** kjøpmannsavrunding, men runder i stedet i partallsretning i situasjoner hvor tallet er midt mellom to alternativer. Dvs., 2.5 vil da rundes ned til 2 fordi 2 er partall, mens 3.5 rundes opp til 4. Det er fornuftige grunner til dette (unngå systematiske feil som man får hvis man alltid runder opp). I noen situasjoner - f.eks. hvis man er kjøpmann - kan det imidlertid være at man faktisk ønsker kjøpmannsavrunding.
# 
# Oppgaven din her er å lage et program som får til kjøpmannsavrunding. Det skal be bruker om å skrive inn et desimaltall, samt ønsket antall desimaler det skal avrundes til - og så foreta denne avrundingen. Dette må da gjøres på annet vis enn å bruke Pythons `round()`-funksjon, siden du f.eks. skal runde 2.5 til 3 (hvis null desimaler) og 2.25 til 2.3 (hvis en desimal) mens `round()` ville runde nedover her. Et par eksempler på kjøring:
# 
#   
# ```python
# Gi inn et desimaltall: 2.5  
# Antall desimaler i avrunding: 0  
# Avrundet til 0 desimaler: 3
# ```
#   
# ```python
# Gi inn et desimaltall: 2.25  
# Antall desimaler i avrunding: 1  
# Avrundet til 1 desimal: 2.3
#     ```
#   
# ```python
# Gi inn et desimaltall: 2500.0  
# Antall desimaler i avrunding: -3  
# Avrundet til -3 desimaler: 3000  
# ```
# 
# Som eksemplet viser skal det også være mulig å gi inn negativt antall desimaler for å få grovere avrunding enn nærmeste heltall. Også da med kjøpmannsavrunding (dvs. 2500 blir 3000, ikke 2000).
# 
# ***Skriv koden din i blokka under.***

# In[5]:


import math

desimaltall = float(input("Gi inn et desimaltall: "))
desimaler = int(input("Antall desimaler i avrunding: "))
faktor = 10 ** desimaler
avrundet = math.floor(desimaltall * faktor + 0.5) / faktor
print('Avrundet til', desimaler, 'desimaler:', avrundet)


# ## b) Avrunding som unngår unøyaktig tallrepresentasjon

# Selv hvis vi er fornøyde med IEEE-standarden for avrunding (heller enn kjøpmannsavrunding), kan `round()` av og til gi overraskende resultater. F.eks.
# 
# * `round(2.50000000000000000001)` gir 2, selv om tallet er litt nærmere 3
# * `round(2.15, 1)` gir 2.1, selv om regelen om å gå mot partall skulle tilsi 2.2
# 
# Begge disse og andre lignende tilfeller skyldes egentlig ikke noen feil ved `round()`-funksjonen, men problemer med selve representasjonen av tall i det binære systemet.
# 
# 2.50000000000000000001 lar seg ikke representere eksakt i maskinen, så den tar det nærmeste den får til, som her blir 2.5 - og dermed vipper `round()` ned.
# 
# 2.15 lar seg heller ikke representere eksakt (i det binære tallsystemet, selv om det kun trengs tre siffer i titallssystemet), det nærmeste maskinen får til er 2.14999999999999999999. Dermed ligger tallet ikke lenger midt imellom men litt nærmere 2.1, så avrunding vipper ned.
# 
# Oppgaven her er å lage et program som klarer å avrunde korrekt selv med slike tall som dette. For å klare oss mest mulig med det som er undervist av pensum hittil, kan heltallsdelen og desimaldelen til tallet vi skal behandle, leses inn hver for seg. Eksempel på kjøring blir da:
# 
#   
# ```
# Oppgi heltallsdelen av tallet (det foran punktum): 2
# Oppgi desimaldelen av tallet (det bak punktum): 5
# Oppgi ønsket antall desimaler i avrunding: 0
# 2.5 avrundet til 0 desimaler blir 2
# 
# Oppgi heltallsdelen av tallet (det foran punktum): 2
# Oppgi desimaldelen av tallet (det bak punktum): 15
# Oppgi ønsket antall desimaler i avrunding: 1
# 2.15 avrundet til 1 desimal blir 2.2
# 
# Oppgi heltallsdelen av tallet (det foran punktum): 2
# Oppgi desimaldelen av tallet (det bak punktum): 500000000000000000001
# Oppgi ønsket antall desimaler i avrunding: 0
# 2.500000000000000000001 avrundet til 0 desimaler blir 3
# ```
# 
# Denne oppgaven går delvis utenfor det som undervist hittil i emnet.
# 
# ***Skriv koden din i blokka under.***

# In[33]:


heltall = int(input('Oppgi heltallsdelen av tallet: '))
desimal = int(input('Oppgi desimaldelen av tallet: '))
avrunder = int(input('Oppgi antall deismaler i avrundingen: '))

def rund(hel, des, n):
    rundetDes = round(des, -1 * (len(str(des)) - n))
    print(rundetDes)
    miniDes = rundetDes / 10 ** len(str(des))
    return hel + miniDes
    
print(str(heltall) + '.' + str(desimal) + ' avrundet til', avrunder, 'desimaler blir', rund(heltall, desimal, avrunder))


# ## c) Strenghåndtering

# Lag et program hvor brukeren skriver inn navnet sitt fra tastaturet etter ledeteksten "Jeg heter:", og la maskinen svare med setningen The name is... som vist i boksen under.
# 
#   
# ```
# Jeg heter: James Bond
# The name is Bond, James Bond
# ```
# 
# Her vil du mest sannsynlig måtte benytte deg av programmeringsmekanismer som ikke er forelest ennå, enten if-setninger, løkker og strengindeksering, eller strengmetoder som `split()` med tilhørende listebehandling. Hvis du vil gjøre det ekstra vanskelig for deg selv (**VALGFRITT**, ikke nødvendig for å få godkjent), prøv å lage et program som også funker for personer med flere enn to navn (f.eks. The name is Hopper, Grace Murray Hopper), men som tar hensyn til at preposisjoner som Von, Van, De, Di er del av etternavnet (f.eks. The name is Von Neumann, John Von Neumann; The name is De Morgan, Augustus De Morgan... dog likevel bare hvis dette kommer i midten, det må fortsatt bli The name is Morrison, Van Morrison). Dessuten, hvis et navn slutter med Jr, Sr eller romertall, er det ikke det siste ordet som er etternavnet men det nest siste: The name is Northug, Petter Northug Jr; The name is Huxtable, Henry Huxtable III.
# 
# ***Skriv koden din i blokka under.***

# In[17]:


name = input('Jeg heter: ')
a = name.split()
surname = ''

# to navn eller færre - rett frem
if len(a) <= 2:
    surname = a[len(a)-1]
# tre eller flere navn
else:
    # Romertall?
    if len(a[len(a)-1]) <= 3:
        # tittel?
        if len(a[len(a)-3]) <= 3 & len(a[len(a)-3]) > 1:
            surname = a[len(a) - 3 : len(a) - 1]
        else:
            surname = a[len(a) - 2]
    else:
        # tittel?
        if len(a[len(a)-2]) <= 3 & len(a[len(a)-2]) > 1:
            surname = a[len(a) - 2 :]
        else:
            surname = a[len(a) - 1]

# Tar listen med ord som ble funnet som etternavn og omgjør til streng
def makeString(liste):
    navnet = ''
    for word in liste:
        navnet += ' ' + word
    return navnet
        
print('The name is ' + makeString(surname) + ', ' + name)

