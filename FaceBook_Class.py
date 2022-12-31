from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class FaceBookBot:
    def __init__(self):
        self.my_service = Service("C:/Zoo_Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.my_service)

    def login_facebook(self, my_email, my_password):
        self.driver.get(url="https://www.facebook.com/")
        sleep(4)
        # enter email - login:
        login = self.driver.find_element(By.ID, "email")
        login.click()
        sleep(1)
        login.send_keys(f"{my_email}")
        # enter password:
        password = self.driver.find_element(By.ID, "pass")
        password.click()
        sleep(1)
        password.send_keys(f"{my_password}")
        sleep(1)
        password.send_keys(Keys.ENTER)
        sleep(10)

    def find_group(self, group_name):
        search_bar = self.driver.find_elements(By.TAG_NAME, "input")[3]
        search_bar.click()
        sleep(1)
        search_bar.send_keys(f"{group_name}")
        sleep(1)
        search_bar.send_keys(Keys.ENTER)
        sleep(5)

    def join_group(self, quantity):
        number = int(quantity) + 4
        group_button = self.driver.find_element(By.LINK_TEXT, "Groups")
        group_button.click()
        sleep(8)
        public_group = self.driver.find_elements(By.TAG_NAME, "input")[5]
        public_group.click()
        sleep(15)
        group_icons = self.driver.find_elements(By.CLASS_NAME, "xuxw1ft")[4:number]
        for icon in group_icons:
            icon.click()
            sleep(2)
