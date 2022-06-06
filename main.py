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
          "10. Wyjscie\n"
          "==========================")

def pobierz_terminarz_lekarza():
    pk=input("Który terminarz pokazać? ")
    url_terminarz="http://127.0.0.1:8000/api/doctor/appointment/created/"
    #token={'Authorization':f'Token {pobierz_token()}'}
    terminarz=requests.get(url_terminarz)
    print(terminarz.text)
