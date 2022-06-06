import requests

#Pobranie tokena uwierzytelniajacego
def pobierz_token():
    url_token="http://127.0.0.1:8000/api_auth/login/"
    token=requests.post(url_token,data={'email':'admin@admin.com','password':'admin'})
    print(token.json())

#pobierz_token()

def menu():
    print("Menu operacji na serwerze \n"
          "==========================\n"
          "1. Lista endpointów na których można wykonać operację\n"
          "2. Wyswietl terminarz lekarza\n"
          "3. Dodaj terminarz lekarza\n"
          "4. Usun terminarz lekarza\n"
          "5. Wyswietl liste pacjentów\n"
          "6. Wyswietl wizyty pacjentów\n"
          "7. Wyswietl wizyte danego pacjenta\n"
          "8. Dodaj wizyte pacjenta\n"
          "9. Usun wizyte pacjenta\n"
          "10. Wyswietl menu\n"
          "11. Wyjscie\n"
          "==========================\n")

def endpointy():
    print("api/patient - lista pacjentów \n"
          "api/patient/appointment - lista umówionych wizyt \n"
          "api/patient/appointment/created/pk - pojedyncza wizyta pacjenta, gdzie pk to identyfikator wizyty\n"
          "api/doctor/appointment/ - terminarz z wizytami lekarza\n"
          "api/doctor/appointment/created/pk - pojedynczy terminarz z wizytą lekarza, gdzie pk to id terminarza\n "
          "===================================================================")


def pobierz_terminarz_lekarza():
    pk=input("Który terminarz pokazać? ")
    url_terminarz="http://127.0.0.1:8000/api/doctor/appointment/created/" + pk
    #token={'Authorization':f'Token {pobierz_token()}'}
    terminarz=requests.get(url_terminarz,
                           params={'q': 'requests+language:python'},)
    dane= terminarz.json()
    print(f'Identyfikator: {dane["id"]}')
    print(f'Pełna nazwa lekarza: {dane["full_name"]}')


def pobierz_liste_pacjentow():
    url_lista="http://127.0.0.1:8000/api/patient"
    lista=requests.get(url_lista)
    print(lista.text)

def pobierz_wizyty_pacjentow():
    url_lista="http://127.0.0.1:8000/api/patient/appointment"
    lista=requests.get(url_lista)
    print(lista.text)

def pobierz_wizyte_pacjenta():
    pk = input("Którą wizytę pokazać? ")
    url_lista="http://127.0.0.1:8000/api/patient/appointment/created/"+pk
    lista=requests.get(url_lista)
    print(lista.text)

menu()
active=True
while active:
    print("Wybierz opcje: ")
    ans = input("")
    if ans=='1':
        endpointy()
        menu()
    elif ans=='2':
        pobierz_terminarz_lekarza()
        menu()
    elif ans=='5':
        pobierz_liste_pacjentow()
        menu()
    elif ans == '6':
        pobierz_wizyty_pacjentow()
        menu()
    elif ans=='7':
        pobierz_wizyte_pacjenta()
        menu()
    elif ans=='11':
        active=False
        break









