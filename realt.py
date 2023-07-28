from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re

"""options"""
options = webdriver.ChromeOptions()

"""user-agent"""
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

"""for ChromeDriver or over"""
options.add_argument("--disable-blink-features=AutomationControlled")

"""1"""
options.add_argument('--headless=new')

# """2"""
# options.headless = True

"""путь к драйверу и браузер"""
service = Service(executable_path='C:/chromedriver/chromedriver')  # указываем путь до драйвера
browser = webdriver.Chrome(service=service, options=options)


class ParsRealt:
    def __init__(self, url: str):
        self.url = url

    """Тут все понятно"""
    def parse(self):
        browser.get(self.url)

    """клик по ссылкам с количеством комнат"""
    def number_of_rooms(self, values):
        if values:
            link_to_apartments = browser.find_element(By.LINK_TEXT, f'{values}-комнатные квартиры') # Links
            link_to_apartments.click()
            """Обработать ошибки"""

    """Пока что тут только фильтрация по цене"""
    def apartment_price_change(self):
        price_filter_button = browser.find_element(By.XPATH, '//*[@id="mainHeader"]/div[2]/div/form/div[4]/div')
        price_filter_button.click()

        min_price = browser.find_element(By.XPATH, '//*[@id="priceFrom"]')
        min_price.send_keys('Вводим значение')

        max_price = browser.find_element(By.XPATH, '//*[@id="priceTo"]')
        max_price.send_keys('Вводим значение')

        price_filter_button.click()

    """Нахождение количества страниц и возврат максимального числа"""
    def number_of_pages(self):

        pages = browser.find_elements(By.XPATH,
                                      '//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[3]/div[2]/div/div')
        pages_str = pages[0].text
        p = re.findall('[0-9]+', pages_str)[5]
        return int(p)

    """Парсинг самих ссылком квартир"""
    def apartment_links(self, values):
        pages_count = ParsRealt.number_of_pages(self)
        links_list = []
        for page in range(1, pages_count + 1):
            browser.get(f"https://realt.by/sale/flats/{values}k/?page={page}")                #1 комната - 1к, 2 - 2к, и тд
            time.sleep(0)
            links = browser.find_elements(By.XPATH,
                                          '//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[3]/div[1]/div/div/div/div/div/div/a')
            for l in links:
                # print(l.get_attribute('href'))
                links_list.append(l.get_attribute('href'))
            print(links_list)
            time.sleep(0)

    def __str__(self):
        pass

    def __repr__(self):
        pass


pars_0 = ParsRealt('https://realt.by/')

pars_0.parse()
pars_0.number_of_rooms(1)
print(pars_0.number_of_pages())
pars_0.apartment_links(1)



# """Дальше старый код)"""
#
#
# url = 'https://realt.by/'
# browser.get(url)
#
# # browser.execute_script('window.scrollTo(0, document.body.scrollHeight);') пролистывание страницы в самый низ
#
# realt_link_1_room = browser.find_element(By.LINK_TEXT, '1-комнатные квартиры')
# realt_link_1_room.click()
# # Так же есть 2,3,4,5 сделаю потом
# print("Открыли страницу с 1-ми квартирами")
#
#
# """Изменение цены квартир"""
# # link = browser.find_element(By.XPATH, '//*[@id="mainHeader"]/div[2]/div/form/div[4]/div')
# # link.click()
# #
# # min_price = browser.find_element(By.XPATH, '//*[@id="priceFrom"]')
# # min_price.send_keys(40_000)
# # max_price = browser.find_element(By.XPATH, '//*[@id="priceTo"]')
# # max_price.send_keys(70_000)
# # link.click()
# # time.sleep(5)
#
# pages = browser.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[3]/div[2]/div/div')
# # pages = browser.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[2]/div[2]/div/div')
#
# """Если цена меняется то div3 это div2"""
# """Если цена неизменна то div3"""
#
# """Парсинг количества страниц"""
# page_str = pages[0].text
# p = re.findall('[0-9]+', page_str)[5]
#
# """Парсинг ссылок"""
# links_list = []
# for p in range(1, int(p) + 1):
#     browser.get(f"https://realt.by/sale/flats/1k/?page={p}")
#     time.sleep(5)
#     links = browser.find_elements(By.XPATH,
#                                   '//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[3]/div[1]/div/div/div/div/div/div/a')
#     for l in links:
#         # print(l.get_attribute('href'))
#         links_list.append(l.get_attribute('href'))
#     print(links_list)
#     time.sleep(5)
#
browser.quit()

"""как закешировать функции на питоне гугл"""
"""gitHub обязательно"""
