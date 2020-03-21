# Digital Era v2

## Use cases
1. Korisnik se registrira/ulogira sa svojim podacima
2. Može kreirati novi predložak za javljanje potencijalnom klijentu
    1. Korisnik sam popunjava podatke o potencijalnom klijentu
    2. Ili upiše web adresu i klikne na izgeneriraj osnovne podatke (može se u to integrirati i analiza postojeće web stranice)
3. Nakon što su podaci o klijentu popunjeni moguće je:
    1. Spremiti nove informacije u listu potencijalnih klijenata
    2. Izgenerirati template za javljanje tom klijentu sa previewom
    3. Direktno poslati mail ili batch mailova klijentima


## Model changes
- Change your models (in models.py).
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.


## Useful resources
- https://wsvincent.com/django-rest-framework-user-authentication-tutorial/ - custom user model authentication