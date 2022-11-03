from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "D:\PYTHON PROJEKTY\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

time_5_min = time.time() + 60 * 5
timeout = time.time() + 5

# Elementy na stronie
cookie = driver.find_element(By.ID, "cookie")


while True:
    cookie.click()

    if time.time() > timeout:
        # Musi byc tutaj poniewaz w przeciwnym razie wywola sie tylko raz
        # Mozna to skrocic do slownika
        cursor = driver.find_element(By.ID, "buyCursor")
        cursor_price = int(cursor.text.split()[2].replace(",", ""))

        grandma = driver.find_element(By.ID, "buyGrandma")
        grandma_price = int(grandma.text.split()[2].replace(",", ""))

        factory = driver.find_element(By.ID, "buyFactory")
        factory_price = int(factory.text.split()[2].replace(",", ""))

        mine = driver.find_element(By.ID, "buyMine")
        mine_price = int(mine.text.split()[2].replace(",", ""))

        shipment = driver.find_element(By.ID, "buyShipment")
        shipment_price = int(shipment.text.split()[2].replace(",", ""))

        alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
        alchemy_lab_price = int(alchemy_lab.text.split()[3].replace(",", ""))

        portal = driver.find_element(By.ID, "buyPortal")
        portal_price = int(portal.text.split()[2].replace(",", ""))

        time_machine = driver.find_element(By.ID, "buyTime machine")
        time_machine_price = int(time_machine.text.split()[3].replace(",", ""))

        elements = [cursor, grandma, factory, mine, shipment, alchemy_lab, portal, time_machine]

        prices = [cursor_price, grandma_price, factory_price, mine_price, shipment_price, alchemy_lab_price, portal_price, time_machine_price]

        cookie_count = driver.find_element(By.ID, "money").text
        if "," in cookie_count:
            cookie_count = cookie_count.replace(",", "")
        money = int(cookie_count)

        affordable = []
        for price in prices:
            if money > price:
                affordable.append(price)
        
        highest_affordable = max(affordable)
        to_click = elements[prices.index(highest_affordable)]
        to_click.click()

        # Dodajemy po kazdym razie by zwikszyc zakres czasowy
        timeout = time.time() + 5
    
    if time.time() > time_5_min:
        cps = driver.find_element(By.ID, "cps").text
        print(cps)
        break

driver.quit()
