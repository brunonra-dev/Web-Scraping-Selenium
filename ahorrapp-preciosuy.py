from selenium import webdriver
from selenium.webdriver.common.by import By


website = 'https://www.precios.uy/sipc2Web/'
path = 'C:/Users/3959/Ahorrap-mati/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)


searchproduct = "arroz"

confirm_botton = driver.find_element(By.XPATH, value='//span/input[@id="form:j_idt59_input"]')
confirm_botton.click()
confirm_botton.send_keys(searchproduct)



buscar_botton = driver.find_element(By.XPATH, value='//*[@id="form:j_idt62"]/span[@class="ui-button-icon-left ui-icon ui-c fa fa-search"]')
buscar_botton.click()

#no anda
carrito_botton = driver.find_element(By.XPATH, value='//*[@id="form:data:0:j_idt79"]/i')
carrito_botton.click()

comparar_botton = driver.find_element(By.XPATH, value='//*[@id="form:j_idt158"]/span[2]')
comparar_botton.click()