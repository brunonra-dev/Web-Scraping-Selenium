from selenium import webdriver
from selenium.webdriver.common.by import By


website = 'https://www.precios.uy/sipc2Web/'
path = 'chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)


searchproduct = "Ta - Ta - Suc. Cordon "

# click "Lista de precios"
driver.find_element(By.XPATH, value='//*[@id="form:j_idt42"]/div[3]/span').click()

# search "Ta - Ta"
driver.implicitly_wait(0.5)
form = driver.find_element(By.XPATH, value='//*[@id="form:j_idt60_input"]')
form.click()
form.send_keys(searchproduct)

search_button = driver.find_element(By.XPATH, value='//*[@id="form:j_idt63"]')
search_button.click()

add_market = driver.find_element(By.XPATH, value='//*[@id="form:data3:0:j_idt92"]')
add_market.click()

driver.implicitly_wait(0.5)
compare_button = driver.find_element(By.XPATH, value='//*[@id="form:j_idt158"]')
compare_button.click()
