def test_user_can_register(driver, open_registration_form, fill_registration_form, registration_form):
    registration_form.register_button.click()

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Add car')]"))
    )
