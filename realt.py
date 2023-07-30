import re

from selenium.webdriver.common.by import By

from setings import options, browser

from constants import url


class ParsRealt:
    def __init__(self, url: str, values: int):
        """url is a link, values is the number of rooms"""

        self.url = url
        self.values = values

    def parse(self):
        """Following a link"""

        browser.get(self.url)

    def number_of_rooms(self):
        """Click on apartment links"""

        if self.values:
            link_to_apartments = browser.find_element(By.LINK_TEXT, f'{self.values}-комнатные квартиры')
            link_to_apartments.click()
            """Обработать ошибки"""

    def apartment_price_change(self):
        """Filtration"""

        price_filter_button = browser.find_element(By.XPATH, '//*[@id="mainHeader"]/div[2]/div/form/div[4]/div')
        price_filter_button.click()

        min_price = browser.find_element(By.XPATH, '//*[@id="priceFrom"]')
        min_price.send_keys(input("Введите минимальное число в долларах"))

        max_price = browser.find_element(By.XPATH, '//*[@id="priceTo"]')
        max_price.send_keys(input("Введите максимальное число в долларах"))

        price_filter_button.click()

    def number_of_pages(self):
        """Finding the number of pages"""

        div_element = 0
        if self.values == 1:
            div_element = 3
        else:
            div_element = 2

        pages = browser.find_elements(By.XPATH,
                                      f'//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[{div_element}]/div[2]/div/div') # 1 комната div_element == 3; 2,3,4 - div_element 2
        pages_str = pages[0].text
        p = re.findall('[0-9]+', pages_str)[5]
        return int(p)

    def apartment_links(self):
        """Apartment link parsing"""

        div_element = 0
        if self.values == 1:
            div_element = 3
        else:
            div_element = 2

        pages_count = ParsRealt.number_of_pages(self)
        links_list = []
        for page in range(1, pages_count + 1):
            browser.get(f"https://realt.by/sale/flats/{self.values}k/?page={page}")
            links = browser.find_elements(By.XPATH,
                                          f'//*[@id="__next"]/div[1]/div[1]/main/div/div/div/div/div[1]/div[{div_element}]/div[1]/div/div/div/div/div/div/a')
            for l in links:
                links_list.append(l.get_attribute('href'))
            return links_list


# pars_0 = ParsRealt(url, 1)
# pars_0.parse()
# pars_0.number_of_rooms()
# pars_0.number_of_pages()
# pars_0.apartment_links()


"""Можно сделать метод для вывода хедерсов сайта, или опшн запрос"""
"""как закешировать функции на питоне гугл"""
