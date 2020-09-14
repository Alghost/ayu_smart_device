import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

filepath = os.path.abspath(__file__)
basedir = os.path.dirname(filepath)
chromedir = os.path.join(basedir, 'Chrome')

opts = webdriver.ChromeOptions()
opts.add_argument(f'user-data-dir={chromedir}')
d = webdriver.Chrome('./chromedriver', options=opts)

try:
    d.get('https://www.instagram.com')

    # input()
    # 로그인 완료한 후 동작해야함

    time.sleep(1)

    elem = d.find_element_by_class_name('eyXLr')
    ac = ActionChains(d)
    ac.move_to_element(elem)
    ac.click()
    ac.send_keys('#파이썬')
    ac.pause(3)
    ac.move_by_offset(0,50)
    ac.click()
    ac.perform()

    time.sleep(4)
    #### END 검색 ####

    article = d.find_element_by_class_name('EZdmt')
    posts = article.find_elements_by_class_name('v1Nh3')
    for post in posts:
        post.click()
        time.sleep(2)

        like_btn = d.find_element_by_class_name('fr66n') 
        innerhtml = like_btn.get_attribute('innerHTML')

        ac = ActionChains(d)
        if '좋아요 취소' not in innerhtml:
            ac.click(like_btn)

        ac.pause(1)
        ac.send_keys(Keys.ESCAPE)
        ac.perform()
        time.sleep(1)

    time.sleep(3)
except:
    traceback.print_exc()
finally:
    d.close()
    d.quit()
