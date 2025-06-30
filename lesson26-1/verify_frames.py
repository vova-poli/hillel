from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Ініціалізація драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://localhost:8000/dz.html")
wait = WebDriverWait(driver, 5)


def verify_frame(frame_id, input_id, secret_value):
    # Перехід у фрейм
    driver.switch_to.frame(frame_id)

    # Введення секретного тексту
    input_field = wait.until(EC.presence_of_element_located((By.ID, input_id)))
    input_field.clear()
    input_field.send_keys(secret_value)

    # Натискання кнопки "Перевірити"
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    # Перехоплення alert
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    print(f"[{frame_id}] alert: {alert_text}")

    # Перевірка успішності
    assert "успішно" in alert_text, f"Помилка у фреймі {frame_id}: {alert_text}"
    alert.accept()

    # Повернення у головну сторінку
    driver.switch_to.default_content()


# Перевірка фрейму 1
verify_frame("frame1", "input1", "Frame1_Secret")

# Перевірка фрейму 2
verify_frame("frame2", "input2", "Frame2_Secret")

print("Верифікація обох фреймів пройдена успішно!")

driver.quit()
