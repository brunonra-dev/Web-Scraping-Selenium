import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask, jsonify


website = 'https://www.disco.com.uy/'
path = 'C:/Users/3959/Ahorrap-mati/chromedriver_win32/chromedriver.exe'
searchproduct = "leche"
driver = webdriver.Chrome(path)
driver.get(website + searchproduct)

confirm_botton = driver.find_element(By.XPATH, value='//*[@id="btnConfirmaSucursal"]')
confirm_botton.click()

resultDict = dict()


providers = ["disco"]

productos = driver.find_elements(by=By.XPATH, value='//li[@class="frescos"]')
#itemPrice = providers.find_element(By.CLASS_NAME, "Product-price")


for produc in productos:
    name = produc.find_element(by=By.XPATH, value='.//h3[@class="Product-title"]').text
    print(name)
    precio = produc.find_element(by=By.XPATH, value='.//div[@class="Product-price"]').text
    print(precio)
    
#resultDict.update({providers[0]: {
 #   "name": itemName.text,
  #  "price": itemPrice.text,

#}})
driver.quit()
print(resultDict)