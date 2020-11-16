#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving9.ipynb">Øving 9</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Generelt%20om%20dictionary.ipynb">Generelt om dictionary</a></li>
#     <li ><a href="Innebygde%20funksjoner%20i%20dictionaries.ipynb">Innebygde funksjoner</a></li>
#     <li ><a href="Generelt%20om%20sets.ipynb">Generelt om sets</a></li>
#     <li ><a href="Generelt%20om%20filbehandling.ipynb">Generelt om filbehandling</a></li>
#     <li ><a href="Osteviruset.ipynb">Osteviruset</a></li>
#     <li ><a href="Bursdagsdatabasen.ipynb">Bursdagsdatabasen</a></li>
#     <li ><a href="Tallak%20teller%20antall%20tall.ipynb">Tallak teller antall tall</a></li>
#     <li class="active"><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#         <li ><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li ><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Opptaksgrenser
# 
# **Læringsmål:**
# 
# * Lese fra filer
# * dictionaries
# 
# **Starting Out with Python:**
# 
# * Kap. 6: Files and Exceptions
# * Kap. 9.1 Dictionaries
# 
# I denne oppgaven skal vi lese inn en fil med opptaksgrensene fra Samordna Opptak.
# 
# Filen er på CSV-format (Comma Separated Values), noe som betyr at hver linje er en liste med felter separert med komma. Tekstfelter er omsluttet av fnutter (").
# 
# * Første felt er studiets navn
# * Andre felt er poenggrensen (enten et tall, eller "Alle" dersom alle kom inn)
# 
# F.eks. linjen: **"NTNU 194459 Antikkens kultur","Alle"** sier at alle som søkte kom inn på Dragvoll-studiet “Antikkens kultur” ved NTNU.
# 
# Hver funksjon i de følgende deloppgavene tar data fra filen **poenggrenser_2011.csv** som input. Derfor er det veldig praktisk å lagre innholdet i en variabel, slik at du slipper å lese den på nytt hver gang.

# ### a)

# Les fra fila `poenggrenser_2011.csv` og lagre innholdet i en variabel.
# 
# ***Skriv koden din i boksen under.***

# In[101]:


file = 'poenggrenser_2011.csv'

poenggrenser = {}

with open(file) as f:
    for line, l in enumerate(f):
        stripped = l.replace('"', '').replace('\n', '') # Fjerner newlines og kvoteringer
        parsed = stripped.split(',') # Splitter i liste
        
        # Omformer til dict, med 1.verdi som key, 2.verdi som value.
        # Om det er et tall blir verdien gjort til en float
        
        try:
            zipped = {parsed[0]: float(parsed[1])}
            # print(parsed[1])
        except:
            zipped = {parsed[0]: parsed[1]}
         
        poenggrenser.update(zipped) # Legger til key:value


# ### b)

# Skriv en funksjon som finner ut hvor mange studier som tok inn alle søkere. 
# 
# ***Husk at du nå i alle deloppgavene kan bruke variabelen du definerte i a så lenge du har kjørt den kodesnutten først!***
# 
# *Eksempel på kjøring av kode:*
# ```python
# Antall studier hvor alle kom inn: 590
# ```
# ***Skriv koden din i boksen under.***

# In[70]:


alle_num = 0

for fag in poenggrenser:
    if poenggrenser[fag] == 'Alle':
        alle_num += 1
        
print('Antalll studier hvor alle kom inn:', alle_num)


# ### b)

# Skriv en funksjon som finner gjennomsnittlig opptaksgrense for NTNU. Ikke ta med studier som tok inn alle søkere.
# 
# *Eksempel på kjøring av kode:*
# ```python
# Gjennomsnittlig opptaksgrense for NTNU var: 46.29
# ```
# ***Skriv koden din i boksen under.***

# In[91]:


poengliste = []

for fag in poenggrenser:
    if type(poenggrenser[fag]) != str and fag[0:4] == 'NTNU':
        poengliste.append(poenggrenser[fag])
        
avg = sum(poengliste) / len(poengliste)

print('Gjennomsnittlig opptaksgrense for NTNU var:', avg)


# #### Hint

# For å sjekke om studiet var på NTNU kan du hente ut de fire første bokstavene i hver linje. Hvis du har en string studie kan du gjøre dette ved å skrive: studie[1:5]

# ### c)

# Skriv en funksjon som finner studiet med laveste opptaksgrense (som IKKE tok inn alle søkere).
# 
# *Eksempel på kjøring av kode:*
# ```python
# Studiet som hadde den laveste opptaksgrensen var: AHO 189343 Industridesign
# ```
# ***Skriv koden din i boksen under.***

# In[100]:


# Lager en dict basert på poenggrenser, strippet av alle keys med verdiem 'Alle'
ikke_alle = {k:v for k,v in poenggrenser.items() if v != 'Alle'}

# Sorterer ikke_alle dict inn i en ny liste
sorterte_grenser = sorted(ikke_alle.items(), key=lambda x: x[1])
laveste_fag = sorterte_grenser[0][0]

print('Studiet som hadde den laveste opptaksgrensen var:', laveste_fag)


# ### d)

# Lag en dictionary som har studiestedet som nøkkel og en liste med dictionaries som verdi. Denne listen med dictionaries skal ha navnet på linjen som nøkkel og opptakspoengene til den tilsvarende linjen som verdi. Dersom en linje har navnet "Fysikk og Matematikk" trenger du kun å ta hensyn til det første ordet, dvs. "Fysikk". 
# 
# **Eksempel på utskrift:**
# 
# ```python
# ATH [{'Kristendom': ' Alle'}, {'Interkulturell': ' Alle'}, {'Musikk': ' Alle'}, {'Teologi': ' Alle'}, {'Kristendom': ' Alle'}, {'Psykologi': ' Alle'}, {'Musikk': ' Alle'}, {'Interkulturell': ' Alle'}, {'Psykologi': ' Alle'}, {'Praktisk': ' Alle'}]
# AHO [{'Arkitekt': '12.3'}, {'Industridesign': '11.7'}]
# BDH [{'Sykepleierutdanning': '45.5'}]
# MF [{'Kristendom/RLE': ' Alle'}, {'Samfunnsfag': ' Alle'}, {'Interkulturell': ' Alle'}, {'Teologi': ' Alle'}, {'Religion': ' Alle'}, {'Ungdom': ' Alle'}, {'Lektor-': ' Alle'}, {'Teologi': ' Alle'}]
# DHS [{'Sykepleierutdanning': '48.3'}, {'Vernepleierutdanning': '41.8'}, {'Sosialt': '49.1'}, {'Sosialt': '42.4'}, {'Ergoterapeututdanning': '32.6'}]
# DMMH [{'Førskolelærerutdanning': '36.3'}, {'Førskolelærer': '39.1'}, {'Førskolelærer': '44'}, {'Førskolelærer': '46.2'}, {'Førskolelærer': ' Alle'}]
# .
# .
# .
# UIT [{'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Sykepleierutdanning': '43.8'}, {'Lærerutdanning': ' Alle'}, {'Lærerutdanning': ' Alle'}, {'Førskolelærerutdanning': ' Alle'}, ....
# ```
# ***Skriv koden din i boksen under.***

# In[126]:


cleaned_dict = {}

for k, v in poenggrenser.items():
    # universitet
    uni = k.split()[0] # splitter opp nøkkelen, og henter første string (universitetet)
    
    # fag og grense
    new_key = k.split()[2] # se over - henter tredje string (første ord i fagnavnet)
    dictpair = {new_key: v} 
    
    # legger enten til i listen over fag og grense, eller lager en ny entry for universitetet
    try: 
        cleaned_dict[uni].append(dictpair)
    except: 
        cleaned_dict.update({uni: [dictpair]})
    
def print_dict(dictionary):
    for key in dictionary:
        print(key + ':', dictionary[key])

print_dict(cleaned_dict)

