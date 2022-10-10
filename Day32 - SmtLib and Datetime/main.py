# import smtplib
#
# my_email = "mail@gmail.com"
# password = "password"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="dawidtest@yahoo.com",
#         msg="Subject:Hello\n\nThis is content of my email"
#     )

import datetime as dt

# Aktualna data i czas z komputera / w ten sposob tworzymy obiekt na ktorym mozna pracowac
now = dt.datetime.now()

# W ten sposob mozemy dostac sie do poszczegolnych danych czasowych
hour = now.hour
minutes = now.minute
seconds = now.second
year = now.year

# W tym przypadku zwracany jest numer dnia tygodnia zamiast jego nazwy / liczone od 0
day_of_week = now.weekday()
print(day_of_week)


# Tworzenie obiektu z konkretna data / mozna nawet wpisac konkretna godzine
date_of_birth = dt.datetime(year=1994, month=3, day=29)
weekday = date_of_birth.weekday()
print(weekday)
