import os
import sys
import time
import signal
from bs4 import BeautifulSoup
from undetected_chromedriver import Chrome,ChromeOptions
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

def handle_sigterm(signum, d):
    print(f"\033[94m[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}]\033[91m[INFO]\033[0m Exit.")
    exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)

ua = UserAgent(platforms='desktop')
user_agent = ua.random

options = ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-extensions')
options.add_argument(f'--user-agent={user_agent}')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--proxy-server='+os.getenv('HTTP_PROXY'))

driver = Chrome(options=options)
driver.get('https://blog.csdn.net/m0_71746299/article/details/125856435')
soup = BeautifulSoup(driver.page_source, 'html.parser')
title = soup.find('h1', id='articleContentId')
print(title.text)
print()
print(soup.find('div', id='content_views').text)

with open('/app/temp/htmls/test.html', 'w') as f:
    f.write(driver.page_source)

content_list = soup.find('div', id='content_views').contents
for i in range(len(content_list)):
    if content_list[i].name is None:
        continue
    print('\033[94m[', i, ']\033[0mlen=', len(content_list[i].text))
    print('\033[94m[name]\033[0m', content_list[i].name)
    print('\033[94m[text]\033[0m', content_list[i].text)
    print('\033[94m[origin]\033[0m', content_list[i])

driver.save_screenshot('/app/temp/screenshots/screenshot.png')

driver.quit()


