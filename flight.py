import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import XLunits


class Test_irctc(unittest.TestCase):
    '''flight search in IRCTC using unittest framework'''


    def test_search_flight(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/Raviraj/Desktop/chromedriver_win32/chromedriver.exe")
        driver = self.driver
        time.sleep(2)
        driver.get("https://www.air.irctc.co.in/")
        driver.maximize_window()
        self.assertEqual(driver.title, "Air Ticket Booking | Book Flight Tickets | Cheap Air Fare - IRCTC Air")

        # -----selecting one way or round ticket-------

        driver.find_element(by=By.XPATH, value="//label[contains(text(),'One Way')]").click()
        time.sleep(5)
        driver.find_element(by=By.XPATH, value="//button[text()='Later']").click()

        # -----  Selecting origin and destination--------

        # Data Driven
        path = "C://Users/Raviraj/Desktop/Data Driven/DDT2.xlsx"
        time.sleep(5)
        rows = XLunits.getRowCount(path, "Sheet1")
        count = 0
        for r in range(2, rows + 1):
            origin = XLunits.readData(path, "Sheet1", r, 1)
            destination = XLunits.readData(path, "Sheet1", r, 2)

            driver.find_element(by=By.XPATH, value="//input [@name= 'From']").click()
            driver.find_element(by=By.XPATH, value="//input [@name= 'From']").send_keys(origin)
            time.sleep(5)
            if origin == "DEL":
                driver.find_element(by=By.XPATH, value="//div[text()='New Delhi (DEL)']").click()
            else:
                driver.find_element(by=By.XPATH, value="//div[text()='Hyderabad (HYD)']").click()

            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//input[@id='stationTo']").click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//input[@id='stationTo']").send_keys(destination)
            time.sleep(5)
            if destination == "BLR":
                driver.find_element(by=By.XPATH, value="//div[text()='Bengaluru (BLR)']").click()
            else:
                driver.find_element(by=By.XPATH, value="//div[text()='Pune (PNQ)']").click()

            # -------  Selecting date-------

            driver.find_element(by=By.XPATH, value="//input[@id='originDate']").click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value="//tbody/tr[4]/td[6]/span[1]").click()

            # ---------------Selecting number of seats, class------------------

            driver.find_element(by=By.XPATH, value="//input[@id='noOfpaxEtc']").click()
            driver.find_element(by=By.XPATH, value="//div[@id='TravellerEconomydropdown']").click()
            time.sleep(2)
            type = Select(driver.find_element(by=By.XPATH, value="//select[@id='travelClass']"))
            type.select_by_index(1)
            time.sleep(2)

            # -----Click on search button

            driver.find_element(by=By.XPATH,
                                value="//body/app-root[1]/app-index[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[6]/button[1]").click()

            if driver.title == "Air Ticket Booking | Book Flight Tickets | Cheap Air Fare - IRCTC Air":
                print("test is passed")
                XLunits.writeData(path, "Sheet1", r, 3, "passed")
            else:
                print("test is failed")
                XLunits.writeData(path, "Sheet1", r, 3, "failed")
                time.sleep(15)
            count = count + 1
            if count < 2:
                driver.back()

        # ------ Taking screenshots---------

        time.sleep(15)

        # driver.save_screenshot("C:\\Users\\Umar\\Documents\\Flight_Search")
        driver.get_screenshot_as_file('flight1.png')
        driver.execute_script("window.scrollBy(0,750)", " ")
        time.sleep(3)
        ## driver.save_screenshot("C:\\Users\\Umar\\Documents\\Flight_Search")
        driver.get_screenshot_as_file('flight2.png')
        driver.execute_script("window.scrollBy(750,1500)", " ")
        time.sleep(3)
        # driver.save_screenshot("C:\\Users\\Umar\\Documents\\Flight_Search")
        driver.get_screenshot_as_file('flight3.png')


if __name__ == "__main__":
    unittest.main()
