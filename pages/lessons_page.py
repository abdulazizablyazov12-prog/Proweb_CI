from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LessonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_lessons = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.lesson_card = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(2) > div.lesson-card > div")
        self.btn_play_video = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.btn_fullscreen = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3)")
        self.press_video = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__actinview")
        self.btn_pause = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button.video-player-proweb__controllers-play")
        self.btn_fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(5)")
        self.btn_back = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div.back-to-less.back-to-less-lesson")


    def click_btn_lessons(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_lessons)).click()

    def click_lesson_card(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.lesson_card)).click()

    def click_btn_play_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_play_video)).click()

    def click_btn_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    def click_press_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.press_video)).click()

    def click_btn_pause(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_pause)).click()

    def click_btn_fullscreen_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen_exit)).click()

    def click_btn_back(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_back)).click()