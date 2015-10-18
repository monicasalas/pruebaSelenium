# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest 
import time

class TestGMail(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get('https://mail.google.com/')
	
	def test_entrar_correo_electronico(self):
		correo = self.driver.find_element_by_id('Email')
		correo.send_keys('janethsalas.luna26@gmail.com')
		correo.send_keys(Keys.RETURN)
		time.sleep(5)
		contra = self.driver.find_element_by_id('Passwd')
		contra.send_keys('zaragoza1994')
		contra.send_keys(Keys.RETURN)
		time.sleep(36)
		entrada=self.driver.find_element_by_id(':3d').click()
if __name__=='__main__':
	unittest.main() 