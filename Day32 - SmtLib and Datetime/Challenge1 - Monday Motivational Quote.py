import smtplib
import datetime as dt
from random import choice

my_email = "dawidtest315@gmail.com"
password = "ahbzwewvvugqmmig"

with open("quotes.txt") as txt:
    quotes = txt.read()
    quotes_list = quotes.split("\n")

random_quote = choice(quotes_list)

now = dt.datetime.now()

if now.weekday() == 4:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="dawidtest@yahoo.com",
            msg=f"Subject:Random Motivational Quote\n{random_quote}"
        )
