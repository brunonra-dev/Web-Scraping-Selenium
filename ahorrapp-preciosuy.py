from selenium import webdriver
from selenium.webdriver.common.by import By


website = 'https://www.precios.uy/sipc2Web/'
path = 'C:/Users/3959/Ahorrap-mati/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)


searchproduct = "tata"

lista_botton = driver.find_element(By.XPATH, value='//*[@id="form:j_idt42"]/div[3]/span')
lista_botton.click()

# no escribe en ese lugar
confirm_botton = driver.find_element(By.XPATH, value='//*[@id="form:panelcomparar"]/div[3]/div[1]/div[2]/span/input[@id="form:j_idt60_input"]')
confirm_botton.click()
confirm_botton.send_keys(searchproduct)



buscar_botton = driver.find_element(By.XPATH, value='//*[@id="form:j_idt62"]/span[@class="ui-button-icon-left ui-icon ui-c fa fa-search"]')
buscar_botton.click()


comparar_botton = driver.find_element(By.XPATH, value='//*[@id="form:j_idt158"]/span[2]')
comparar_botton.click()