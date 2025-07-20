import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from nova_poshta_tracker import NovaPoshtaTracker

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_nova_poshta_tracking(driver):
    ttn_number = "20400459661341"
    expected_keyword = "отриман"

    tracker = NovaPoshtaTracker(driver)
    tracker.open_page()
    tracker.enter_ttn_number(ttn_number)
    status = tracker.get_status_text()

    assert expected_keyword in status.lower(), f"Статус має містити '{expected_keyword}', але отримано: {status}"
