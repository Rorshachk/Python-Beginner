from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'ipad'


def index_page(page):
    browser.get("http://taobao.com")
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
    print(input)
    submit = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
    input.send_keys('美食')
    submit.click()


index_page(1)
