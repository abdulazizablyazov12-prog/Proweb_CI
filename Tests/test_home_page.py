import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.auth_page import AuthPage
from pages.home_page import HomePage

def test_home_page_chrome(driver_chrome):
    driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()                    # Login page
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
        sleep(2)
    except:
        pass

    home_page = HomePage(driver_chrome)         # Home Page video test
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    home_page.click_btn_pause()
    time.sleep(2)
    home_page.click_btn_fullscreen_exit()
    sleep(2)


    home_page.click_profile_icon()          # Exit from account
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_home_page_firefox(driver_firefox):
    driver_firefox.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_firefox)
    auth_page.click_btn_uz()                     # Login Page
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
        sleep(2)
    except:
        pass

    home_page = HomePage(driver_firefox)  # Home Page video test
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen_firefox()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    home_page.click_btn_pause()
    time.sleep(2)
    home_page.click_fullscreen_exit_firefox()
    sleep(2)

    home_page.click_profile_icon()  # Exit from account
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_home_page_safari(driver_safari):
    driver_safari.get('https://my.proweb.uz/log-in?q=/home')
    auth_page = AuthPage(driver_safari)
    auth_page.click_btn_uz()  # Login Page test
    time.sleep(2)
    auth_page.enter_login("998998866405")
    time.sleep(2)
    auth_page.click_btn_login()
    time.sleep(2)
    auth_page.enter_password("1280!@#$Aa")
    time.sleep(2)
    auth_page.click_btn_submit()
    time.sleep(2)
    try:
        auth_page.click_dropdown_session()
        time.sleep(2)
        auth_page.click_btn_finish()
    except:
        pass

    home_page = HomePage(driver_safari)     # Home Page video test
    home_page.click_video_instruction()
    time.sleep(2)
    home_page.click_btn_fullscreen()
    time.sleep(10)
    home_page.click_press_video()
    time.sleep(2)
    ActionChains(driver_safari).send_keys(Keys.SPACE).perform()
    time.sleep(2)
    home_page.press_escape()
    time.sleep(2)

    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()
