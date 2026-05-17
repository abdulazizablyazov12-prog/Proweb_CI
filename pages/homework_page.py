from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class HomeworkPage:
    def __init__(self, driver):
        self.driver = driver
        self.group_card = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2)")
        self.homework_page_chrome = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(4)")
        self.homework_page_firefox = (By.CSS_SELECTOR, "div.tab-header__item:nth-child(4) > span:nth-child(1) > span:nth-child(1)")
        self.homework_card = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div > div > div:nth-child(2) > div.work-dropdown.homework-card_drop.grow > div > div")
        self.go_to_homework = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div > div > div:nth-child(2) > div.work-dropdown.homework-card_drop.grow.homework-card_drop-active > div.work-dropdown-content > div > button")
        self.text_area = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label > textarea")
        self.text_area_firefox = (By.CSS_SELECTOR, ".material-input__input")
        self.text_area_safari = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > div > div > label > textarea")
        self.text_send = (By.CSS_SELECTOR, "#app > div > div.container.homework-page-container > div > div > div > div.solved-homework__materials > div.message-input.relative.solved-homework-input > button")

    def click_group_card(self):
        wait = WebDriverWait(self.driver, 10)
        # 1. Сначала находим элемент и сохраняем его в переменную element
        element = wait.until(EC.element_to_be_clickable(self.group_card))
        # 2. ВОТ ЭТА СТРОКА опустит страницу так, чтобы элемент оказался строго по СЕНТРУ экрана:
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        # 3. Делаем клик
        element.click()

    def click_homework_page_chrome(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.homework_page_chrome))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        time.sleep(1)
        element.click()

    def click_homework_page_firefox(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.homework_page_firefox))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        time.sleep(1)
        element.click()

    def click_btn_homework_card(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.homework_card))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_btn_go_to_homework(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.go_to_homework))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_input_text_area(self, text_area):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.text_area)).send_keys(text_area)

    def enter_text_firefox(self, text_area_firefox):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.text_area_firefox)).send_keys(text_area_firefox)

    def enter_text_safari(self, text_area_safari):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.text_area_safari)).send_keys(text_area_safari)

    def click_btn_text_send(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.text_send)).click()
