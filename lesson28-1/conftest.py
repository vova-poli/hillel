import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.registration_form import RegistrationForm
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def registration_form(driver):
    return RegistrationForm(driver)

@pytest.fixture
def open_registration_form(main_page):
    main_page.sign_up_button.click()

@pytest.fixture
def fill_registration_form(driver, registration_form):
    from random import randint
    email = f"testuser{randint(1000,9999)}@example.com"
    registration_form.name_input.send_keys("Test")
    registration_form.last_name_input.send_keys("User")
    registration_form.email_input.send_keys(email)
    registration_form.password_input.send_keys("TestPass123")
    registration_form.repeat_password_input.send_keys("TestPass123")
    return email
