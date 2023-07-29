from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""Launch Chrome driver"""
options = webdriver.ChromeOptions()

"""user-agent"""
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

"""Removing the graphical interface"""
options.add_argument("--disable-blink-features=AutomationControlled")

"""Disable Interface"""
options.add_argument('--headless=new')

# """2"""
# options.headless = True

"""Path to the driver. browser"""
service = Service(executable_path='C:/chromedriver/chromedriver')  # указываем путь до драйвера
browser = webdriver.Chrome(service=service, options=options)
