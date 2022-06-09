import json
import requests

#Pobranie tokena uwierzytelniajacego
def pobierz_token():
    url_token="http://127.0.0.1:8000/api_auth/login/"
    token=requests.post(url_token,data={'email':'admin@admin.com','password':'admin'})
    print(token.json())

#pobierz_token()

def menu():
    print("==========================\n"
          "Menu operacji na serwerze \n"
          "==========================\n"
          "1. Lista endpointów na których można wykonać operację\n"
          "2. Wyswietl wszystkie terminarze\n"
          "3. Wyswietl terminarz lekarza\n"
          "4. Dodaj terminarz lekarza\n"
          "5. Usun terminarz lekarza\n"
          "6. Modyfikuj terminarz lekarza\n"
          "7. Wyswietl liste pacjentów\n"
          "8. Wyswietl wizyty pacjentów\n"
          "9. Wyswietl wizyte danego pacjenta\n"
          "10. Dodaj wizyte pacjenta\n"
          "11. Usun wizyte pacjenta\n"
          "12. Modyfikuj wizyte pacjenta\n"
          "13. Wyswietl menu\n"
          "14. Wyjscie\n"
          "==========================\n")

def endpointy():
    print("api/patient - lista pacjentów \n"
          "api/patient/appointment - lista umówionych wizyt \n"
          "api/patient/appointment/created/pk - pojedyncza wizyta pacjenta, gdzie pk to identyfikator wizyty\n"
          "api/doctor/appointment/ - terminarz z wizytami lekarza\n"
          "api/doctor/appointment/created/pk - pojedynczy terminarz z wizytą lekarza, gdzie pk to id terminarza\n "
          "===================================================================")

def wszystkie_terminarze():
    url_terminarze = "http://127.0.0.1:8000/api/doctor/appointment"
    wszystkie = requests.get(url_terminarze,
                             params={'q': 'requests+language:python'})
    dane= wszystkie.json()
    for terminarz in dane:
        print(f'Identyfikator: {terminarz["id"]}')
        print(f'Imię i nazwisko doktora: {terminarz["full_name"]}')
        print(f'Lokalizacja gabinetu: {terminarz["location"]}')
        print(f'Godziny otwarcia gabinetu od: {terminarz["start_time"]} do {terminarz["end_time"]}')
        print(f'Specjalizacja medyczna: {terminarz["qualification_name"]}')
        print(f'Nazwa instytutu: {terminarz["institute_name"]}')
        print(f'Nazwa szpitala: {terminarz["hospital_name"]}')
        print(f'Wydział: {terminarz["department"]}\n')



def pobierz_terminarz_lekarza():
    pk=input("Który terminarz pokazać? ")
    url_terminarz="http://127.0.0.1:8000/api/doctor/appointment/created/" + pk

    terminarz=requests.get(url_terminarz,
                           params={'q': 'requests+language:python'})
    dane= terminarz.json()
    print(f'Identyfikator: {dane["id"]}')
    print(f'Imię i nazwisko doktora: {dane["full_name"]}')
    print(f'Lokalizacja gabinetu: {dane["location"]}')
    print(f'Godziny otwarcia gabinetu od: {dane["start_time"]} do {dane["end_time"]}')
    print(f'Specjalizacja medyczna: {dane["qualification_name"]}')
    print(f'Nazwa instytutu: {dane["institute_name"]}')
    print(f'Nazwa szpitala: {dane["hospital_name"]}')
    print(f'Wydział: {dane["department"]}\n')


def utworz_terminarz():
    full_name = input("Imię i nazwisko: ")
    image=input("Zdjecie (domyślnie puste): ")
    location=input("Miasto, Kraj: ")
    start=input("Godzina otwarcia gabinetu: ")
    end=input("Godzina zamknięcia gabinetu: ")
    quali=input("Nazwa kwalifikacji: ")
    institute=input("Instytut: ")
    hospital=input("Nazwa szpitala: ")
    department=input("Wydział szpitala: ")
    created_at=input("Data stworzenia terminarza (domyślnie teraz): ")
    user=input("ID użytkownika: ")

    url_terminarz = "http://127.0.0.1:8000/api/doctor/appointment/"

    data = {
            'full_name': full_name,
            'image': image,
            'location':location,
            'start_time':start,
            'end_time':end,
            'qualification_name':quali,
            'institute_name':institute,
            'hospital_name':hospital,
            'department':department,
            'created_at':created_at,
            'user':user
            }

    requests.post(url_terminarz, data=data)
    print("Utworzono terminarz\n")

def usun_terminarz():
    pk=input("Podaj identyfikator terminarza który chcesz usunąć: ")
    r = requests.delete('http://127.0.0.1:8000/api/doctor/appointment/created/'+ pk)

    print(r.json())

def modyfikuj_terminarz():
    pk=input("Podaj identyfikator terminarza który chcesz modyfikowac: ")

    full_name = input("Imię i nazwisko: ")
    image = input("Zdjecie (domyślnie puste): ")
    location = input("Miasto, Kraj: ")
    start = input("Godzina otwarcia gabinetu: ")
    end = input("Godzina zamknięcia gabinetu: ")
    quali = input("Nazwa kwalifikacji: ")
    institute = input("Instytut: ")
    hospital = input("Nazwa szpitala: ")
    department = input("Wydział szpitala: ")
    created_at = input("Data stworzenia terminarza (domyślnie teraz): ")
    user = input("ID użytkownika: ")

    url_terminarz = "http://127.0.0.1:8000/api/doctor/appointment/created/" + pk

    data = {
        'full_name': full_name,
        'image': image,
        'location': location,
        'start_time': start,
        'end_time': end,
        'qualification_name': quali,
        'institute_name': institute,
        'hospital_name': hospital,
        'department': department,
        'created_at': created_at,
        'user': user
    }

    requests.put(url_terminarz,data={
        'full_name': full_name,
        'image': image,
        'location': location,
        'start_time': start,
        'end_time': end,
        'qualification_name': quali,
        'institute_name': institute,
        'hospital_name': hospital,
        'department': department,
        'created_at': created_at,
        'user': user
    })
    print("Zmodyfikowano terminarz\n")

def pobierz_liste_pacjentow():
    url_lista="http://127.0.0.1:8000/api/patient"
    lista=requests.get(url_lista,
                       params={'q': 'requests+language:python'})

    pacjenci = lista.json()
    for pacjent in pacjenci:
        print(f"Imię i nazwisko: {pacjent['full_name']}")
        print(f"Numer telefonu pacjenta: {pacjent['phone_number']}")
        print(f"Opis dolegliwości: {pacjent['message']}")
        print(f"Data stworzenia wizyty: {pacjent['date']}\n")

def pobierz_wizyty_pacjentow():
    url_lista="http://127.0.0.1:8000/api/patient/appointment"
    wizyty=requests.get(url_lista,
                       params={'q': 'requests+language:python'})
    dane_wizyt = wizyty.json()
    for wizyta in dane_wizyt:
        print(f'Identyfikator: {wizyta["id"]}')
        print(f'Imię i nazwisko pacjenta: {wizyta["full_name"]}')
        print(f'Opis dolegliwości: {wizyta["message"]}')
        print(f'Numer telefonu pacjenta: {wizyta["phone_number"]}')
        print(f'Data złożenia wizyty: {wizyta["date"]}')
        print(f'Numer identyfikacyjny terminarza lekarskiego: {wizyta["appointment"]}\n')

def pobierz_wizyte_pacjenta():
    pk = input("Którą wizytę pokazać? ")
    url_wizyta="http://127.0.0.1:8000/api/patient/appointment/created/"+pk
    wizyta=requests.get(url_wizyta,
                       params={'q': 'requests+language:python'})
    dane = wizyta.json()
    print(f'Identyfikator: {dane["id"]}')
    print(f'Imię i nazwisko pacjenta: {dane["full_name"]}')
    print(f'Opis dolegliwości: {dane["message"]}')
    print(f'Numer telefonu pacjenta: {dane["phone_number"]}')
    print(f'Data złożenia wizyty: {dane["date"]}')
    print(f'Numer identyfikacyjny terminarza lekarskiego: {dane["appointment"]}\n')

def utworz_wizyte():
    full_name = input("Imię i nazwisko: ")
    message = input("Opis dolegliwości: ")
    phone= input("Numer telefonu pacjenta: ")
    date = input("Data stworzenia wizyty: (domyślnie teraz): ")
    user = input("ID pacjenta wstawiającego: ")
    appointment = input("Numer terminarza do przywiązania: ")

    url_wizyta = "http://127.0.0.1:8000/api/patient/appointment/"

    data = {
        'full_name': full_name,
        'message': message,
        'phone_number': phone,
        'date': date,
        'user': user,
        'appointment': appointment
    }

    requests.post(url_wizyta, data=data)
    print("Utworzono wizytę \n")


def usun_wizyte():
    pk = input("Podaj identyfikator wizyty, którą chcesz usunąć: ")
    r = requests.delete('http://127.0.0.1:8000/api/patient/appointment/created/'+pk)

    print(r.json())

def modyfikuj_wizyte():
    pk = input("Podaj identyfikator wizyty, którą chcesz modyfikować: ")


menu()
active=True
while active:
    print("Wybierz opcje: ")
    ans = input("")
    if ans=='1':
        endpointy()
        menu()
    elif ans=='2':
        wszystkie_terminarze()
        menu()
    elif ans=='3':
        pobierz_terminarz_lekarza()
        menu()
    elif ans=='4':
        utworz_terminarz()
        menu()
    elif ans=='5':
        usun_terminarz()
        menu()
    elif ans == '6':
        modyfikuj_terminarz()
        menu()
    elif ans=='7':
        pobierz_liste_pacjentow()
        menu()
    elif ans == '8':
        pobierz_wizyty_pacjentow()
        menu()
    elif ans=='9':
        pobierz_wizyte_pacjenta()
        menu()
    elif ans=='10':
        utworz_wizyte()
        menu()
    elif ans=='11':
        usun_wizyte()
        menu()
    elif ans == '12':
        modyfikuj_wizyte()
        menu()
    elif ans=='13':
        menu()
    elif ans=='14':
        active=False
        break











