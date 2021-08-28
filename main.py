from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

options = Options()
options.add_argument(r'user-data-dir=' + os.environ.get('chromeUserPath'))

browser = webdriver.Chrome(options=options)
browser.get('https://www.google.com')

wait = WebDriverWait(browser, 5)

search_bar = wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")))
search_bar.send_keys('whatsapp web')

enter_action = ActionChains(browser)
enter_action.send_keys(Keys.ENTER)

enter_action.perform()

whatsapp_link = wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/h3[1]")))
whatsapp_link.click()