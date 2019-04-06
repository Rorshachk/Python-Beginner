from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException


browser = webdriver.Chrome()
'''
browser.get('http://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('Python')
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
'''
'''
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_name('q')
input_third = browser.find_element_by_css_selector('#q')
input_fourth = browser.find_element_by_xpath('//*[@id="q"]')
input_fifth = browser.find_element(By.ID, 'q')
lis = browser.find_elements_by_css_selector('.service-bd li')
'''

# print(lis)
# print(input_first, input_second, input_third, input_fourth, input_fifth)

'''
input = browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
botton = browser.find_element_by_class_name('btn-search')
botton.click()
'''

'''
url = 'http://www.runoob.com//try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to_frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
'''
'''
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
'''
'''
url = 'https://www.zhihu.com/explore'
browser.get(url)

logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
'''

'''
browser.implicitly_wait(10)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
'''

'''
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, '.btn-search')))
print(input, button)
'''
'''
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.org')
browser.back()
time.sleep(1)
browser.forward()
'''

'''
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie(
    {'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
'''

'''
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.python.org')
'''


try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No element')
