import pandas
import smtplib
import datetime as dt
import random

data = pandas.read_csv("birthdays.csv")
birthday_month_list = data["month"].to_list()
birthday_day_list = data["day"].to_list()

PLACEHOLDER = "[NAME]"
letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(letter_list)

now = dt.datetime.now()
month = now.month
day = now.day

name_row = data[data.day == day]
# W ten sposob uzyskamy konkretna wartosc z rzedu / ta metoda zwraca tylko wartosc a nie Series
to_mail = str(name_row.email.values[0])
name = str(name_row.name.values[0])


my_email = "mail@gmail.com"
password = "password"

if month in birthday_month_list and day in birthday_day_list:
    with open(f"./Letter Templates/{random_letter}") as letter:
        letter = letter.read()
        new_letter = letter.replace(PLACEHOLDER, name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_mail,
            msg=f"Subject:Happy Birthday!\n{new_letter}"
        )
