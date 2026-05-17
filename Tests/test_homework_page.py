import time
from time import sleep

from pages.homework_page import HomeworkPage
from pages.auth_page import AuthPage

def test_homework_page_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_chrome)
    auth_page.click_btn_uz()  # Login page
    sleep(2)
    auth_page.enter_login("")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("")
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

    homework_page = HomeworkPage(driver_chrome)
    homework_page.click_group_card()
    sleep(2)
    homework_page.click_homework_page_chrome()
    sleep(2)
    homework_page.click_btn_homework_card()
    sleep(3)
    homework_page.click_btn_go_to_homework()
    sleep(2)
    homework_page.click_input_text_area("test")
    sleep(2)
    homework_page.click_btn_text_send()
    sleep(2)

def test_homework_page_firefox(driver_firefox):
    driver_firefox.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_firefox)
    auth_page.click_btn_uz()  # Login page
    sleep(2)
    auth_page.enter_login("")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_firefox_password("")
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

    homework_page = HomeworkPage(driver_firefox)
    homework_page.click_group_card()
    sleep(2)
    homework_page.click_homework_page_firefox()
    sleep(2)
    homework_page.click_btn_homework_card()
    sleep(3)
    homework_page.click_btn_go_to_homework()
    sleep(2)
    homework_page.enter_text_firefox("test")
    sleep(2)
    homework_page.click_btn_text_send()
    sleep(2)

def test_homework_page_safari(driver_safari):
    driver_safari.get("https://my.proweb.uz/log-in?q=/home")
    auth_page = AuthPage(driver_safari)
    auth_page.click_btn_uz()  # Login page
    sleep(2)
    auth_page.enter_login("")
    sleep(2)
    auth_page.click_btn_login()
    sleep(2)
    auth_page.enter_password("")
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

    homework_page = HomeworkPage(driver_safari)
    homework_page.click_group_card()
    sleep(2)
    homework_page.click_homework_page_chrome()
    sleep(2)
    homework_page.click_btn_homework_card()
    sleep(3)
    homework_page.click_btn_go_to_homework()
    sleep(2)
    homework_page.enter_text_safari("test")
    sleep(2)
    homework_page.click_btn_text_send()
    sleep(2)
