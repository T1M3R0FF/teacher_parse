import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from data import email, pwd


def login_and_search():
    driver = webdriver.Chrome()
    driver.get('https://lk.repetitor.ru/order/teacher')
    repetitor_button = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, '//a[@href="/login/signin"]'))
    )
    repetitor_button.click()

    email_input = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'loginform-email'))
    )
    email_input.send_keys(email)

    pwd_input = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'loginform-password'))
    )
    pwd_input.send_keys(pwd)
    pwd_input.send_keys(Keys.ENTER)

    while True:
        try:
            button = WebDriverWait(driver, 5).until(
                ec.presence_of_element_located((By.CLASS_NAME, 'btn-success'))
            )
            if button:
                button.click()
                payment_button = WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.CLASS_NAME, 'btn-primary'))
                )
                if payment_button:
                    payment_button.click()
                    time.sleep(10)
                    orders_button = WebDriverWait(driver, 10).until(
                        ec.presence_of_element_located((By.XPATH, '//a[@href="/order/teacher"]'))
                    )
                    orders_button.click()
        except TimeoutException:
            driver.refresh()


def main():
    login_and_search()


main()
