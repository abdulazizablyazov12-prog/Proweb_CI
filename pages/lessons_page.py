from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LessonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.group_card = (By.CSS_SELECTOR, "#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2)")
        self.btn_lessons = (By.CSS_SELECTOR, "#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(2)")
        self.lesson_card = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(2) > div.lesson-card > div")
        self.lesson_video2 = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(3) > div.lesson-card > div")
        self.lesson_video3 = (By.CSS_SELECTOR, "#app > div > div.container.container_mobile > div > div > div.new-lessons_content > div > div:nth-child(5) > div.flex.gap20 > div:nth-child(1) > div.lesson-card > div")
        self.five_star = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div.videolesson__general-footer-rating.mb10 > div > div > div > span:nth-child(5)")
        self.send_star = (By.CSS_SELECTOR, "#dialog > div > div > div > div > div > button")
        self.btn_play_video = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.btn_fullscreen = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3)")
        self.btn_fullscreen_firefox = (By.CSS_SELECTOR, ".baseavatar_fullscreen")
        self.btn_pause = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-left > button")
        self.btn_fullscreen_exit = (By.CSS_SELECTOR, "#app > div > div.videolesson > div > div:nth-child(2) > div > div:nth-child(3) > div.video-player-proweb > div > div.video-player-proweb__controlls > div.video-player-proweb__controllers > div.video-player-proweb__controllers-right > button:nth-child(3)")
        self.fullscreen_exit_firefox = (By.CSS_SELECTOR, ".baseavatar_fullscreen-exit")

    def click_group_card(self):
        wait = WebDriverWait(self.driver, 10)
        # 1. Сначала находим элемент и сохраняем его в переменную element
        element = wait.until(EC.element_to_be_clickable(self.group_card))
        # 2. ВОТ ЭТА СТРОКА опустит страницу так, чтобы элемент оказался строго по СЕНТРУ экрана:
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        # 3. Делаем клик
        element.click()

    def click_btn_lessons(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.btn_lessons))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_lesson_video2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.lesson_video2)).click()

    def click_lesson_video3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.lesson_video3)).click()

    def click_lesson_card(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.lesson_card))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
        element.click()

    def click_five_star(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.five_star)).click()

    def click_send_star(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.send_star)).click()

    def click_btn_play_video(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_play_video)).click()

    def click_btn_fullscreen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen)).click()

    def click_btn_fullscreen_firefox(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen_firefox)).click()

    def press_escape(self):
        """сброс полного экрана видео"""

        # ЭТАП 1: Возвращаем фокус на плеер
        try:
            # Мы ищем кнопку паузы (или любой элемент внутри плеера)
            video_element = self.driver.find_element(*self.btn_pause)

            # Создаем цепочку действий ActionChains
            from selenium.webdriver.common.action_chains import ActionChains
            actions = ActionChains(self.driver)

            # Перемещаем курсор мышки на этот элемент и КЛИКАЕМ по нему.
            # Клик возвращает фокус клавиатуры внутрь плеера!
            actions.move_to_element(video_element).click().perform()
        except:
            # Если вдруг кнопка не нашлась, мы не роняем тест ошибкой,
            # а просто идем дальше (для этого нужен блок try-except)
            pass

    def press_escape_safari(self):
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

    def click_btn_pause(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_pause)).click()

    def click_btn_fullscreen_exit(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.btn_fullscreen_exit)).click()

    def click_fullscreen_exit_firefox(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.fullscreen_exit_firefox)).click()