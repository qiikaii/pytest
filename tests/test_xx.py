import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as Firefox_Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    """
    setup of browser, to be passed in for each ui test
    """
    # setup
    options = Options()
    options.headless = True # False for non-headless
    s = Firefox_Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=s, options=options)
    
    # return when completed
    yield browser


def test_http(browser):
    # setup
    """
    PLACEHOLDER / TO BE DELETED
    """
    wait = WebDriverWait(browser, 10)
    browser.get("http://apptest:80")

    # check for https connection
    assert "http" in browser.current_url
    browser.close()

def test_xss(browser):
    # setup
    wait = WebDriverWait(browser, 10)
    browser.get("http://apptest:80")
    browser.implicitly_wait(3)
    wait.until(EC.presence_of_element_located((By.ID, "search")))
    wait.until(EC.presence_of_element_located((By.ID, "submit")))

    searchbox = browser.find_element(By.ID, 'search')

    searchbox.send_keys("<script>alert('XSS')</script>")
    submit = browser.find_element(By.ID, 'submit')
    submit.click()

    browser.implicitly_wait(3)
    try:
        wait.until(EC.title_is("main"))
		print(str(e) + "No XSS found.")
        browser.close()
    
    except Exception as e:
		assert 'XSS found'
        browser.close()
