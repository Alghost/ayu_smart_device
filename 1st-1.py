import time
import traceback
from selenium import webdriver

d = webdriver.Chrome('./chromedriver')

try:
    d.get('https://news.naver.com')
    elem = d.find_element_by_id('right.ranking_contents')
    lis = elem.find_elements_by_tag_name('li')
    for li in lis:
        a_tag = li.find_element_by_tag_name('a')
        print(a_tag.text)
except:
    traceback.print_exc()
finally:
    d.close()
    d.quit()
