from selenium import webdriver
from selenium.webdriver.common.by import By


website = 'https://www.precios.uy/sipc2Web/'
path = 'chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

#space at the end required
market = "Ta - Ta - Suc. Cordon "
market_products = {}
market_products[market] = {}
market_products[market]["products"] = {}

# click "Lista de precios"
driver.find_element(By.XPATH, value='//*[@id="form:j_idt42"]/div[3]/span').click()

# search "Ta - Ta"
driver.implicitly_wait(0.5)
form = driver.find_element(By.XPATH, value='//*[@id="form:j_idt60_input"]')
form.click()
form.send_keys(market)

#click "buscar" button
search_button = driver.find_element(By.XPATH, value='//*[@id="form:j_idt63"]')
search_button.click()

#click "cart" button
add_market = driver.find_element(By.XPATH, value='//*[@id="form:data3:0:j_idt92"]')
add_market.click()

# refresh page (if?) map not load
driver.refresh()

#wait and click on "comparar precios" button
driver.implicitly_wait(0.5)
compare_button = driver.find_element(By.XPATH, value='//*[@id="form:j_idt158"]')
compare_button.click()

#get all table elements
rows = driver.find_elements(by=By.XPATH, value='//*[@id="form:resultado_data"]/tr')

#get all products and save all in a dictionary
for i in rows:
    split_name = i.text.split(",")
    split_crap = split_name[1].split("\n$")
    split_price_date = split_crap[1].split(" - ")
    market_products[market]["products"][split_name[0]] = {}
    market_products[market]["products"][split_name[0]]["price"] = split_price_date[0]
    market_products[market]["products"][split_name[0]]["update_at"] = split_price_date[1]

print(market_products)
