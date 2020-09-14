import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome('./chromedriver')

res = []
try:
    d.get('https://www.naver.com')

    elem = d.find_element_by_id('query')
    elem.send_keys('한양대학교')
    elem.send_keys(Keys.RETURN)
    # btn = d.find_element_by_id('search_btn')
    # btn.click()

    news_area = d.find_element_by_class_name('_prs_nws_all')
    lis = news_area.find_elements_by_xpath('./ul/li')
    for li in lis:
        title_tag = li.find_element_by_class_name('_sp_each_title')
        title = title_tag.text
        link = title_tag.get_attribute('href')
        publisher_tag = li.find_element_by_class_name('_sp_each_source')
        publisher = publisher_tag.text.replace('언론사 선정', '')

        date_tag = li.find_element_by_class_name('txt_inline')
        date = date_tag.text.replace(publisher_tag.text, '')
        date = date.replace('네이버뉴스 보내기', '').strip()

        dds = li.find_elements_by_xpath('./dl/dd')
        content_tag = dds[1]
        content = content_tag.text

        res.append((title, link, publisher, date, content))

    with open('result.csv', 'w') as f:
        for row in res:
            f.write(','.join(row) + '\n')

    time.sleep(2)

except:
    traceback.print_exc()
finally:
    d.close()
    d.quit()
