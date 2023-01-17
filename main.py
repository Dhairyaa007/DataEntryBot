from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

HOUSE_PRICE = []
HOUSE_WEBLINK = []
HOUSE_ADDRESS = []
HOUSE_RENT = {}
COUNT = 0


class DataEntryBot:

    def __init__(self):
        self.chrome_driver_path = Service("C://Program Files (x86)/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.driver.maximize_window()
        self.kijiji_data_collector()
        self.google_auto_formfiller()
        self.driver.quit()

    def kijiji_data_collector(self):
        global HOUSE_WEBLINK, HOUSE_RENT
        self.driver.get('https://www.kijiji.ca/b-apartments-condos/ottawa/1+bedroom/c37l1700185a27949001?ll=45.334905'
                        '%2C-75.724101&address=Nepean%2C+Ottawa%2C+ON&radius=5.0&price=__1400')

        # Need to create a list with Price, Address and Listing Link
        price = self.driver.find_elements(By.CLASS_NAME, 'price')
        for value in price:
            price_value = value.text
            HOUSE_PRICE.append(price_value)
        # print(HOUSE_PRICE)

        address = self.driver.find_elements(By.CLASS_NAME, 'nearest-intersection')
        for value in address:
            address_value = value.text
            HOUSE_ADDRESS.append(address_value)
        # print(HOUSE_ADDRESS)

        weblink = self.driver.find_elements(By.CLASS_NAME, 'title')
        for value in weblink:
            weblink_value = value.get_attribute('href')
            HOUSE_WEBLINK.append(weblink_value)
            HOUSE_WEBLINK = [value for value in HOUSE_WEBLINK if value]
        # print(HOUSE_WEBLINK)

    # HOUSE RENT DICTIONARY
    #     print(f"House Address: {len(HOUSE_ADDRESS)}\n House Price: {len(HOUSE_PRICE)}\n House Weblink: {len(HOUSE_WEBLINK)}")
    #     for n in range(len(HOUSE_PRICE)):
    #         HOUSE_RENT[n] = {
    #             "Address": HOUSE_ADDRESS[n],
    #             "Price": HOUSE_PRICE[n],
    #             "Weblink": HOUSE_WEBLINK[n]
    #         }
    #     print(HOUSE_RENT)

    def google_auto_formfiller(self):
        global COUNT
        time.sleep(3)
        self.driver.get('https://forms.gle/WdUpMP6nVeNLZeAv6')
        time.sleep(3)

        while COUNT < len(HOUSE_PRICE):
            house_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                             '2]/div/div[1]/div/div[1]/input')
            house_address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                               '2]/div/div[1]/div/div[1]/input')
            house_weblink = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
                                                               '2]/div/div[1]/div/div[1]/input')
            submit_btn = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div['
                                                            '1]/div/span/span')

            house_price.send_keys(HOUSE_PRICE[COUNT])
            house_address.send_keys(HOUSE_ADDRESS[COUNT])
            house_weblink.send_keys(HOUSE_WEBLINK[COUNT])
            submit_btn.click()
            COUNT += 1
            time.sleep(3)
            self.google_auto_formfiller()


ibot = DataEntryBot()
