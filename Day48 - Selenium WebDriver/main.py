from selenium import webdriver
# Rozwiazanie z kursu juz nie dziala / WYkorzystywane jest to do wyszukiwania elementow na stronie
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\PYTHON PROJEKTY\chromedriver\chromedriver.exe"

# Tworzenie obiektu sterownika przegladarki / moze byc inna przegladarka jesli mamy odpowiedni webdriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Otworzenie strony przy uzyciu sterownika
driver.get("https://www.python.org/")

# Uzyskanie elementu z wykorzystaniem XPATH / XPATH elementu uzyskamy klikajac prawym klawiszem myszy na dany element i kopiujac XPATH
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

driver.quit()
