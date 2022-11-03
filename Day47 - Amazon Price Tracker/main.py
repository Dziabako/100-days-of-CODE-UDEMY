import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = "https://www.amazon.pl/MINIS-FORUM-EliteMini-HX90-DisplayPort/dp/B09LMFR9ST/ref=sr_1_25?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1JSXDGSKP3WWD&keywords=mini+pc&qid=1667224067&qu=eyJxc2MiOiI2LjY4IiwicXNhIjoiNC42NyIsInFzcCI6IjMuNDYifQ%3D%3D&sprefix=mini+pc%2Caps%2C143&sr=8-25"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(url=url, headers=headers)
website_text = response.text

soup = BeautifulSoup(website_text, "lxml")

price_span = soup.find(name="span", class_="a-offscreen")
price = price_span.getText().split("zł")[0]
price_list = price.split("\xa0")
price_float = float("".join(price_list).replace(",", "."))

print(price_float)

# Dziala lecz ten mail juz usunalem ze wzgledu na dziwny spam
my_email = "dawidtest315@gmail.com"
password = "ahbzwewvvugqmmig"

if price_float < 4500.0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Price Alert!\n\nMINIS FORUM EliteMini HX90 Mini PC AMD Ryzen 9 Price is below 4500PLN"
        )
