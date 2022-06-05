from selenium import webdriver
from selenium.webdriver.common.by import By


website = 'https://www.precios.uy/sipc2Web/'
path = 'chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

#space at the end required
products_list = ['Jabón de tocador Rexona', 'Té negro en saquitos La Virginia', 'Hamburguesas carne vacuna Burgy (3 unidades)', 'Agua de mesa Con Gas - Matutina ', 'Arvejas en conserva Nidemar', 'Lechuga Crespa', 
'Naranja Navel ', 'Lechuga Mantecosa', 'Harina trigo 000 Cololó', 'Zapallo Calabacín ', 'Aceite de maíz - Salad', 'Arroz blanco - Vidarroz', 'Jabón de tocador Palmolive', 'Mayonesa común Uruguay', 
'Algodón Zig Zag Cisne', 'Harina trigo 000 Cañuelas', 'Galletitas al agua Maestro Cubano', 'Harina de maíz Puritas', 'Huevos colorados Prodhin', 'Jabón para ropa en barra Nevex multi.', 'Té negro en saquitos Hornimans', 'Arroz Blanco - Aruba ', 'Manzana Red Deliciosa ', 'Arvejas en conserva Cololó', 'Azúcar blanco Bella Unión', 'Harina de maíz Presto Pronta Arcor', 'Azúcar blanco Azucarlito', 'Sal fina yodada fluorada Urusal', 'Arroz blanco - Green Chef', 'Huevos colorados El Jefe']
products = {}


for product in products_list:
    print(product)

    # search product
    form = driver.find_element(By.XPATH, value='//*[@id="form:j_idt59_input"]')
    form.click()
    
    form.send_keys(product)
    products[product] = {}

    #click "buscar" button
    search_button = driver.find_element(By.XPATH, value='//*[@id="form:j_idt62"]')
    search_button.click()

    #click "cart" button
    driver.implicitly_wait(0.5)
    add_market = driver.find_element(By.XPATH, value='//*[@id="form:data:0:j_idt79"]')
    add_market.click()

    # product description //*[@id="form:canasta_list"]/li/div/div[1]/span[2]
    des1 = driver.find_element(By.XPATH, value='//*[@id="form:canasta_list"]/li/div/div[1]/span[2]').text
    des2 = driver.find_element(By.XPATH, value='//*[@id="form:canasta_list"]/li/div/div[1]/span[3]').text

    products[product]["Description"] = des1 + " " + des2

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
        # split_name = i.text.split(",")
        # split_crap = split_name[1].split("\n$")
        # split_price_date = split_crap[1].split(" - ")
        # market_products[market]["products"][split_name[0]] = {}
        # market_products[market]["products"][split_name[0]]["price"] = split_price_date[0]
        # market_products[market]["products"][split_name[0]]["update_at"] = split_price_date[1]
        print(i.text)
    
    driver.find_elements(by=By.XPATH, value='//*[@id="form:canasta:0:j_idt114"]').click()

print(products)