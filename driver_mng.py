from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class DriverManager:
    def __init__(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)  # Veya Firefox kullanıyorsanız: webdriver.Firefox()
        self.driver.get("https://orteil.dashnet.org/experiments/cookie/")
        self.the_cookie = self.driver.find_element(By.CSS_SELECTOR, "div #cookie")
        self.my_money = int(self.driver.find_element(By.CSS_SELECTOR, "#money").text)

        self.list_of_purchase = []

    def find_element(self):
        self.list_of_purchase.clear()
        #scraping current money amount
        self.my_money = int(self.driver.find_element(By.CSS_SELECTOR, "#money").text.replace(",", ""))
        #scraping current price
        purchase_list = self.driver.find_elements(By.CSS_SELECTOR, "#store div b")
        #to update list of purchase in proper format (int)
        for n in range(0, len(purchase_list) - 1):
            #phyton doesn't read 2,000 numb as a float or int, it returns string

            self.list_of_purchase.append(int(purchase_list[n].text.split()[-1].replace(",", "")))


        #find exact index in purchase_list
        index = self.list_of_purchase.index(self.max_price_find())
        if int(purchase_list[index].text.split()[-1].replace(",", "")) <= self.my_money:
            purchase_list[index].click()
            print("Buy")
        else:
            print("Broke")

    def max_price_find(self):
        # to find highest numb in the purchase list.
        purchable = [x for x in self.list_of_purchase if x <= self.my_money]
        print(purchable)
        if purchable:
            return max(purchable)
        else:
            return None