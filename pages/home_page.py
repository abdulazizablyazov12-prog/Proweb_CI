from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.video_instruction = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div.home-card.pointer")
        self.btn_fullscreen = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(5)")
        self.btn_fullscreen_firefox = (By.CSS_SELECTOR, ".baseavatar_fullscreen")
        self.press_video = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__actinview")
        self.btn_pause = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button.video-player-proweb__controllers-play")
        self.fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.home-instruction > div > div.home-instruction__content-main > div > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(5)")
        self.fullscreen_exit_firefox = (By.CSS_SELECTOR, ".baseavatar_fullscreen-exit")
        self.profile_icon = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar > div")
        self.btn_exit = (By.CSS_SELECTOR, "#app > div > div.inforation > div > div > div:nth-child(4) > div")
        self.confirm_exit = (By.CSS_SELECTOR, "#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2)")

    def click_video_instruction(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.video_instruction))
        # 2. ВОТ ЭТА СТРОКА опустит страницу так, чтобы элемент оказался строго по СЕНТРУ экрана:
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        # 3. Делаем клик
        element.click()

    def click_btn_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    def click_btn_fullscreen_firefox(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen_firefox)).click()

    def click_press_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.press_video)).click()

    def click_btn_pause(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_pause)).click()

    def press_escape(self):
        """Супер-надежный метод для выхода из полноэкранного режима в Safari и Chrome"""
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys

        # Шлем Esc напрямую в браузер через ActionChains
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        # Дополнительно шлем в тег body
        try:
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        except:
            pass

    def click_btn_fullscreen_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_exit)).click()

    def click_fullscreen_exit_firefox(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_exit_firefox)).click()

    def click_profile_icon(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def click_btn_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_exit)).click()

    def click_confirm_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.confirm_exit)).click()


