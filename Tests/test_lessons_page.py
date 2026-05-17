import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.lessons_page import LessonsPage

def test_lessons_page_chrome(driver_chrome):
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()                     # Login page
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("prowebqa!@#$")
    sleep(2)
    auth_page.click_btn_submit()
    sleep(3)
    try:
        auth_page.click_dropdown_session()
        time.sleep(2)
        auth_page.click_btn_finish()
        time.sleep(5)
    except:
        pass

    lessons_page = LessonsPage(driver_chrome)       #Lessons video
    lessons_page.click_group_card()
    time.sleep(2)
    lessons_page.click_btn_lessons()
    time.sleep(2)
    lessons_page.click_lesson_card()
    time.sleep(2)
    try:
        lessons_page.click_five_star()              # Star for video
        time.sleep(2)
        lessons_page.click_send_star()
        time.sleep(2)
    except:
        pass
    lessons_page.click_btn_play_video()
    time.sleep(2)
    lessons_page.click_btn_fullscreen()
    time.sleep(10)
    lessons_page.press_escape()
    time.sleep(3)
    lessons_page.click_btn_fullscreen_exit()
    time.sleep(2)

    home_page = HomePage(driver_chrome)         # Exit from account
    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_lessons_page_firefox(driver_firefox):
    driver_firefox.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_firefox)
    auth_page.click_btn_uz()                     # Login page
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_firefox_password("prowebqa!@#$")
    sleep(2)
    auth_page.click_btn_submit()
    sleep(5)
    try:
        auth_page.click_dropdown_session()
        time.sleep(2)
        auth_page.click_btn_finish()
        sleep(5)
    except:
        pass

    lessons_page = LessonsPage(driver_firefox)       #Lessons video
    lessons_page.click_group_card()
    time.sleep(2)
    lessons_page.click_btn_lessons()
    time.sleep(2)
    lessons_page.click_lesson_video2()
    time.sleep(2)
    try:
        lessons_page.click_five_star()
        time.sleep(2)
        lessons_page.click_send_star()
        time.sleep(2)
    except:
        pass
    lessons_page.click_btn_play_video()
    time.sleep(2)
    lessons_page.click_btn_fullscreen_firefox()
    time.sleep(10)
    lessons_page.press_escape()
    time.sleep(3)
    lessons_page.click_fullscreen_exit_firefox()
    time.sleep(2)

    home_page = HomePage(driver_firefox)         # Exit from account
    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_lessons_page_safari(driver_safari):
    driver_safari.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_safari)
    auth_page.click_btn_uz()                     # Login page
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("prowebqa!@#$")
    sleep(2)
    auth_page.click_btn_submit()
    sleep(5)
    try:
        auth_page.click_dropdown_session()
        time.sleep(2)
        auth_page.click_btn_finish()
        sleep(5)
    except:
        pass

    lessons_page = LessonsPage(driver_safari)       #Lessons video
    lessons_page.click_group_card()
    time.sleep(2)
    lessons_page.click_btn_lessons()
    time.sleep(2)
    lessons_page.click_lesson_video3()
    time.sleep(2)
    try:
        lessons_page.click_five_star()
        time.sleep(2)
        lessons_page.click_send_star()
        time.sleep(2)
    except:
        pass
    lessons_page.click_btn_play_video()
    time.sleep(2)
    lessons_page.click_btn_fullscreen()
    time.sleep(10)
    lessons_page.press_escape_safari()
    time.sleep(2)
    ActionChains(driver_safari).send_keys(Keys.SPACE).perform()
    time.sleep(2)

    home_page = HomePage(driver_safari)         # Exit from account
    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()