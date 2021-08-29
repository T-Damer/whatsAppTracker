from macheronte.whatsapp.enums.browsers import Browsers
from macheronte.whatsapp.enums.status import Status

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from PIL import Image
from io import BytesIO

import os.path
import time
import ast

class WhatsappClient:

    def __init__(self, browser: Browsers, profile_name: str):
        options = Options()

        if browser == Browsers.CHROME:
            self.__webdriver = webdriver.Chrome(chrome_options=options)

        self.__chat = None

        self.__enter_action = ActionChains(self.__webdriver)
        self.__enter_action.send_keys(Keys.ENTER)

        self.__esc_action = ActionChains(self.__webdriver)
        self.__esc_action.send_keys(Keys.ESCAPE)

        my_path = os.path.abspath(os.path.dirname(__file__))
        self.__path = os.path.join(my_path, 'xpaths.cfg')

    def connect(self) -> bool:
        try:
            self.__webdriver.get("https://web.whatsapp.com")
            self.__wait = WebDriverWait(self.__webdriver, 5)
        except:
            return False
        return True

    def close(self) -> bool:
        try:
            self.__webdriver.quit()
        except:
            return False
        return True

    def minimize_window(self):
        self.__webdriver.minimize_window()

    def maximize_window(self):
        self.__webdriver.maximize_window()

    def is_logged(self) -> bool:
        try:
            self.__webdriver.find_element_by_xpath(self.__get_xpath("IS_LOGGED"))
        except:
            return False
        return True

    def save_qrcode(self, filename: str) -> bool:
        im = self.__get_img_by_variables("QR_CODE")

        if im != None:
            im.save(filename)
            return True
        return False

    def save_header(self, filename: str) -> bool:
        im = self.__get_img_by_variables("HEADER")

        if im != None:
            im.save(filename)
            return True
        return False

    def get_header(self) -> bool:
        im = self.__get_img_by_variables("HEADER")

        if im == None:
            return None

        width, height = im.size
        im = im.crop((0, 0, width - width * 0.5, height))

        b = BytesIO()
        im.save(b, "PNG")
        b.seek(0)
        return b

    def open_chat(self, target: str) -> bool:
        pass

    def get_user_status(self, target: str) -> bool:
        pass

    def send_message(self, target: str, message: str) -> bool:
        pass

    def __get_img_by_variables(self, variable_name: str) -> str:
        pass

    def __get_xpath(self, variable_name: str) -> str:
        pass
