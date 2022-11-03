from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\PYTHON PROJEKTY\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

dates_selenium = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_selenium = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")

dates = [date.text for date in dates_selenium]
events = [event.text for event in events_selenium[1:]]

event_dict = {}
for n in range(len(dates)):
    event_dict[n] = {
        "time": dates[n],
        "name": events[n]
    }

print(event_dict)

driver.quit()