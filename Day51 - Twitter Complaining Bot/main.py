import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DOWNLOAD_SPEED = 300
UPLOAD_SPEED = 50
CHROME_DRIVER_PATH = "D:\PYTHON PROJEKTY\chromedriver\chromedriver.exe"
TWITTER_LOGIN = "LOGIN"
TWITTER_PASSWORD = "HASLO"
TWITTER_USERNAME = "USERNAME"

url = "https://twitter.com/"
speed_test = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
        self.driver.maximize_window()

    def get_internet_speed(self, speed_test):
        self.driver.get(url=speed_test)

        time.sleep(5)
        accept_cookie = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_cookie.click()

        close_info = self.driver.find_element(By.CLASS_NAME, "notification-dismiss")
        close_info.click()

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        time.sleep(60)

        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def tweet_at_provider(self, twitter_page):
        self.driver.get(twitter_page)

        time.sleep(5)

        login_button = self.driver.find_element(By.CLASS_NAME, "css-901oao.css-16my406.css-1hf3ou5.r-poiln3.r-a023e6.r-rjixqe.r-bcqeeo.r-qvutc0")
        login_button.click()

        time.sleep(5)

        log_in = self.driver.find_element(By.CLASS_NAME, "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        log_in.send_keys(TWITTER_LOGIN)
        log_in.send_keys(Keys.ENTER)

        time.sleep(5)

        username = self.driver.find_element(By.CLASS_NAME, "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)

        time.sleep(5)

        password = self.driver.find_element(By.CLASS_NAME, "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(5)

        tweet = f"Hey Orange Polska! Why my internet speed is {self.down} for dwonload and {self.up} for upload when I am paying for {DOWNLOAD_SPEED} download and {UPLOAD_SPEED} upload?"

        tweet_space = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        tweet_space.send_keys(tweet)

        time.sleep(5)

        tweet_button = self.driver.find_element(By.CLASS_NAME, "css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr")
        tweet_button.click()

        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

twitter_bot.get_internet_speed(speed_test)
print(f"""
Down: {twitter_bot.down}
Up: {twitter_bot.up}""")

if twitter_bot.down < DOWNLOAD_SPEED or twitter_bot.up < UPLOAD_SPEED:
    twitter_bot.tweet_at_provider(url)
