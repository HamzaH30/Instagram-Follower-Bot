import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
SIMILAR_ACCOUNT = "lewishamilton"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH))

    def login(self):
        # Open Instagram Login page
        self.driver.get("https://www.instagram.com/accounts/login/")

        # Waiting for elements to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
        # Enter username
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(USERNAME)

        # Enter password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        # Click enter
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        # Go to Similar Target Account's instagram page
        # Wait for elements to load
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search Input']")))
        # Search
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search Input']")
        search_input.send_keys(SIMILAR_ACCOUNT)

        # Wait for elements to load
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/lewishamilton/']")))
        # Click on the account in search results
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/lewishamilton/']").click()



    def follow(self):
        pass


insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
