import time
from time import sleep

from pages.auth_page import AuthPage
from pages.home_page import HomePage


def test_auth_chrome(driver_chrome):   # Chrome browser Positive Test
    try:
        driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    except TimeoutException:
        print("Сайт не загрузился за 30 секунд, пробуем обновить страницу...")
        driver_chrome.refresh()

    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()                     # Login page test
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("proweb!@#$")
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

    home_page = HomePage(driver_chrome)         # Exit from Home page
    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_invalid_auth_chrome(driver_chrome):    # Chrome browser Negative Test
    try:
        driver_chrome.get('https://my.proweb.uz/log-in?q=/home')
    except TimeoutException:
        print("Сайт не загрузился за 30 секунд, пробуем обновить страницу...")
        driver_chrome.refresh()
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()
    sleep(2)
    auth_page.enter_login("998998866405")       # True phone number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("prowebqa!@14#$")   # False password
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    auth_page.click_btn_back()
    sleep(2)
    auth_page.enter_login("998998866400")       # False number test
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)

def test_auth_firefox(driver_firefox):      # FireFox browser Positive Test
    try:
        driver_firefox.get('https://my.proweb.uz/log-in?q=/home')
    except TimeoutException:
        print("Сайт не загрузился за 30 секунд, пробуем обновить страницу...")
        driver_firefox.refresh()

    auth_page = AuthPage(driver_firefox)
    auth_page.click_btn_uz()                        # Login Page test
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_firefox_password("proweb!@#$")
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    try:
        auth_page.click_dropdown_session()
        sleep(2)
        auth_page.click_btn_finish()
        sleep(4)
    except:
        pass

    home_page = HomePage(driver_firefox)         # Exit from Home page
    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_invalid_auth_firefox(driver_firefox):    # FireFox browser Negative Test
    try:
        driver_firefox.get('https://my.proweb.uz/log-in?q=/home')
    except TimeoutException:
        print("Сайт не загрузился за 30 секунд, пробуем обновить страницу...")
        driver_firefox.refresh()

    auth_page = AuthPage(driver_firefox)
    auth_page.click_btn_uz()
    sleep(2)
    auth_page.enter_login("998998866405")       # True phone number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_firefox_password("0!@#21f3qe")   # False password
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
    try:
        driver_safari.get('https://my.proweb.uz/log-in?q=/home')
    except TimeoutException:
        print("Сайт не загрузился за 30 секунд, пробуем обновить страницу...")
        driver_safari.refresh()

    auth_page = AuthPage(driver_safari)
    auth_page.click_btn_uz()  # Login Page test
    sleep(2)
    auth_page.enter_login("998998866405")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("proweb!@#$")
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

    home_page = HomePage(driver_safari)         # Exit from Home page
    home_page.click_profile_icon()
    sleep(2)
    home_page.click_btn_exit()
    sleep(2)
    home_page.click_confirm_exit()

def test_invalid_auth_safari(driver_safari):    # Safari browser Negative Test
    try:
        driver_safari.get('https://my.proweb.uz/log-in?q=/home')
    except TimeoutException:
        print("Сайт не загрузился за 30 секунд, пробуем обновить страницу...")
        driver_safari.refresh()

    auth_page = AuthPage(driver_safari)
    auth_page.click_btn_uz()
    sleep(2)
    auth_page.enter_login("998998866405")       # True phone number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("120!@#a123")   # False password
    sleep(2)
    auth_page.click_btn_submit()
    sleep(2)
    auth_page.click_btn_back()
    sleep(2)
    auth_page.enter_login("998998866210")       # False number
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
