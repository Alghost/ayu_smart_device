import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

filepath = os.path.abspath(__file__)
basedir = os.path.dirname(filepath)
chromedir = os.path.join(basedir, 'Chrome')

opts = webdriver.ChromeOptions()
opts.add_argument(f'user-data-dir={chromedir}')
d = webdriver.Chrome('./chromedriver', options=opts)

try:
    d.get('https://cafe.naver.com/joonggonara')

    elem = d.find_element_by_id('topLayerQueryInput')
    elem.send_keys('닌텐도')
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

    iframe = d.find_element_by_id('cafe_main')
    d.switch_to.frame(iframe)

    current_page = 1
    links = []
    while True:
        if current_page > 5:
            break
        article_boards = d.find_elements_by_class_name('article-board')
        article_board = article_boards[1]

        trs = article_board.find_elements_by_xpath('./table/tbody/tr')
        for tr in trs:
            link = tr.find_element_by_class_name('article').get_attribute('href')
            links.append(link)

        current_page += 1
        if current_page % 10  == 1:
            next_page = d.find_element_by_class_name('pgR')
        else:
            next_page = d.find_element_by_link_text(str(current_page))
        next_page.click()

    time.sleep(3)
except:
    traceback.print_exc()
finally:
    d.close()
    d.quit()
