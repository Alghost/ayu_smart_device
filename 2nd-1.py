import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome('./chromedriver')

fd = open('results.csv', 'w', encoding='utf-8')

try:
    d.get('https://cafe.naver.com/joonggonara')


    elem = d.find_element_by_id('topLayerQueryInput')
    elem.send_keys('닌텐도')
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

    iframe = d.find_element_by_id('cafe_main')
    d.switch_to.frame(iframe)

    current_page = 1
    while True:
        if current_page > 12:
            break
        article_boards = d.find_elements_by_class_name('article-board')
        article_board = article_boards[1]

        trs = article_board.find_elements_by_xpath('./table/tbody/tr')
        for tr in trs:
            cols = []
            cols.append(tr.find_element_by_class_name('inner_number'))
            cols.append(tr.find_element_by_class_name('article'))
            cols.append(tr.find_element_by_class_name('p-nick'))
            cols.append(tr.find_element_by_class_name('td_date'))
            cols.append(tr.find_element_by_class_name('td_view'))

            # 지능형리스트
            cols = [c.text.strip() for c in cols]
            # 제네레이터
            # cols = (c.text.strip() for c in cols)
            # print(cols)
            # print(['숫자', '이름', '작성자', '시간', '조회'])
            # print(*cols)
            # print('숫자', '이름', '작성자', '시간', '조회')
            fd.write(','.join(cols) + '\n')

        current_page += 1
        if current_page % 10  == 1:
            next_page = d.find_element_by_class_name('pgR')
        else:
            next_page = d.find_element_by_link_text(str(current_page))
        next_page.click()

except:
    traceback.print_exc()
finally:
    fd.close()
    d.close()
    d.quit()
