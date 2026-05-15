import time
from time import sleep

from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.lessons_page import LessonsPage

def test_auth_chrome(driver_chrome):   # Chrome browser Positive Test
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()                     # Login page test
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("1280!@#$Aa")
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    try:
        auth_page.click_dropdown_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass

    home_page = HomePage(driver_chrome)            # Home Page exit test
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    home_page.click_btn_pause()
    time.sleep(2)
    home_page.click_btn_fullscreen_exit()

    home_page.click_logo()
    time.sleep(2)
    home_page.click_group_card()
    time.sleep(2)

    lessons_page = LessonsPage(driver_chrome)
    lessons_page.click_btn_lessons()
    time.sleep(2)
    lessons_page.click_lesson_card()
    time.sleep(2)
    lessons_page.click_btn_play_video()
    time.sleep(2)
    lessons_page.click_btn_fullscreen()
    time.sleep(10)
    lessons_page.click_press_video()
    time.sleep(2)
    lessons_page.click_btn_pause()
    time.sleep(2)
    lessons_page.click_btn_fullscreen_exit()
    time.sleep(2)
    lessons_page.click_btn_back()
    time.sleep(2)

    home_page.click_profile_icon()
    time.sleep(2)
    home_page.click_btn_exit()
    time.sleep(2)
    home_page.click_confirm_exit()

def test_invalid_auth_chrome(driver_chrome):    # Chrome browser Negative Test
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()
    sleep(2)
    auth_page.enter_login("998998866405")       # True phone number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("1280!@#$Aa123")   # False password
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    auth_page.click_btn_back()
    sleep(2)
    auth_page.enter_login("998998866400")       # With False number test
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)

def test_auth_firefox(driver_firefox):      # FireFox browser Positive Test
    driver_firefox.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_firefox)
    auth_page.click_btn_uz()                        # Login Page test
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_firefox_password("1280!@#$Aa")
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    try:
        auth_page.click_dropdown_session()
        sleep(2)
        auth_page.click_btn_finish()
    except:
        pass

    home_page = HomePage(driver_firefox)             # Home Page test
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    home_page.click_btn_pause()
    time.sleep(2)
    home_page.click_btn_fullscreen_exit()


    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_invalid_auth_firefox(driver_firefox):    # FireFox browser Negative Test
    driver_firefox.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_firefox)
    auth_page.click_btn_uz()
    sleep(2)
    auth_page.enter_login("998998866405")       # True phone number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_firefox_password("1280!@#a123")   # False password
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    auth_page.click_btn_back()
    sleep(2)
    auth_page.enter_login("998998866410")       # False number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)

def test_auth_safari(driver_safari):     # Safari browser Positive Test
    driver_safari.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_safari)
    auth_page.click_btn_uz()                        # Login Page test
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_firefox_password("1280!@#$Aa")
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    try:
        auth_page.click_dropdown_session()
        sleep(2)
        auth_page.click_btn_finish()
    except:
        pass

    home_page = HomePage(driver_safari)             # Home Page test
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    home_page.click_btn_pause()
    time.sleep(2)
    home_page.click_btn_fullscreen_exit()


    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_invalid_auth_safari(driver_safari):    # Safari browser Negative Test
    driver_safari.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_safari)
    auth_page.click_btn_uz()
    sleep(2)
    auth_page.enter_login("998998866405")       # True phone number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_firefox_password("120!@#a123")   # False password
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    auth_page.click_btn_back()
    sleep(2)
    auth_page.enter_login("998998866210")       # False number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)


