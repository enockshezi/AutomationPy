from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

PATH = r'C:\Program Files\chromedriver.exe'

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(PATH)
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://enockshezi.github.io/Development-Portfolio/")
