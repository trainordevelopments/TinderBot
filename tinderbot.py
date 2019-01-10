from selenium import webdriver
import time
import sys


class TinderBot:
    def __init__(self):
        self.phoneNum = raw_input("Enter your phone number: ")
        # Open Google Chrome
        self.driver = webdriver.Chrome()

    def wait(self, timetosleep):
        time.sleep(timetosleep)

    def login(self):
        self.driver.get("https://tinder.com/")
        self.wait(5)
        elem_phoneNumButton = self.driver.find_element_by_xpath("//button[@aria-label='Log in with phone number']")
        elem_phoneNumButton.click()
        self.wait(3)
        elem_phoneNum = self.driver.find_element_by_xpath("//input[@name='phone_number']")
        elem_phoneNum.send_keys(self.phoneNum)
        elem_continueButton = self.driver.find_element_by_xpath("//span[text() = 'Continue']/ancestor::button")
        elem_continueButton.click()
        self.wait(2)
        inputCode = raw_input("Enter the code sent to your phone: ")
        elem_phoneInput = self.driver.find_element_by_xpath("//input[@type='number']")
        elem_phoneInput.send_keys(inputCode)
        elem_continueButton2 = self.driver.find_element_by_xpath("//span[text() = 'Continue']/ancestor::button")
        self.driver.execute_script("arguments[0].click();", elem_continueButton2)
        self.wait(2)
        elem_postLoginContinueButton = self.driver.find_element_by_xpath("//span[text() = 'Allow']/ancestor::button")
        elem_postLoginContinueButton.click()
        self.wait(2)
        elem_notInterested = self.driver.find_element_by_xpath("//span[text() = 'Not interested']/ancestor::button")
        elem_notInterested.click()
        self.wait(15)
        self.likePhotos()

    def likePhotos(self):
        while True:
            try:
                elem_likeButton = self.driver.find_element_by_xpath(
                    "//button[contains(@class, 'button Lts($ls-s) Z(0) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) recsGamepad__button D(b) Bgc(#fff) Wc($transform) recsGamepad__button--like Scale(1.1):h')]")
                elem_likeButton.click()
                self.wait(2)
                continue
            except Exception as e:
                print(e.message)
                #self.driver.close()
                #sys.exit()


TinderBot().login()
