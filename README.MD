# PROJEKT-FLASK APLIKACIJA

## Aplikacija se sastoji od više stranica koje predstavljaju nekakvu fiktivnu tvrtku kojoj je osnovna djelatnost web dizajn, IT usluge, prodaja i predstavljanje novih proizvoda i svijeta umjetnosti.
## Na pocetnoj stranici(index.html) nalazi se link Log in, on vodi na stranicu koja sadrži polja za unos podataka za pristup.Uneseni username i password pritiskom na tipku submit spremaju se u zasebnu tablicu imena "saves" kojoj se može pristupiti iz izbornika na stranici koja se prikaže nakon pritiska na tipku submit. 
## U izborniku aftlog stranice također se nalaze link koji vodi na stranicu za unos podataka o novom korisniku(add.html), link za stranicu na kojoj se nalazi prikaz tablice "users" u koju se spremaju podaci korisnika te također i polje za brisanje podataka iz tablice, unosom id-a i pritiskom tipke submit briše se redak iz tablice koji pripada unesenom id-u.

# Pokretanje aplikacije
## 1.Instaliramo virtualno okruženje u CMD ili Poweshell-u ( py -m venv venv ili python -m venv venv)
## 2.Ulazimo u direktorij Scripts unutar venv foldera kako bi ga aktivirali (venv\Scripts\activate)
## 3.Instalacija sa requirements (pip install -r requirements.txt)
## 4.set FLASK_APP=app.py
## 5.set FLASK_DEBUG=1
## 6.flask run
## 7.Otvoriti browser te upisati(http://127.0.0.1:5000/)

