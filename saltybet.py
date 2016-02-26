# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from datetime import datetime

class T(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.saltybet.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t(self):
        driver = self.driver
        val = 0
		
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("span").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("EMAIL ADDRESS")
        driver.find_element_by_id("pword").clear()
        driver.find_element_by_id("pword").send_keys("PASSWORD")
        driver.find_element_by_css_selector("input.graybutton").click()
		
        while True:
			while True:
				try:
					if "Bets are OPEN!" == driver.find_element_by_id("betstatus").text: break
				except: pass
				time.sleep(1)
			else: self.fail("time out")
			
			driver.find_element_by_id("interval10").click()
			val = driver.find_element_by_id("wager").get_attribute("value")
			
			if (int(val) > 5000):
				print("Done at: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
				break
				
			driver.find_element_by_id("player1").click()
				
			while True:
				try:
					if "Bets are locked until the next match." == driver.find_element_by_id("betstatus").text: break
				except: pass
				time.sleep(1)
			else: self.fail("time out")
		
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
