from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options= webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
S=Service("E:/chromedriver_win32/chromedriver/chromedriver_win32 (5)/chromedriver.exe")
driver=webdriver.Chrome(options=options,service=S)
driver.maximize_window()
driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/product/cap")
# time.sleep(3)
AddCartBtn=driver.find_element(By.NAME,"add-to-cart")
driver.execute_script("arguments[0].scrollIntoView();", AddCartBtn)
AddCartBtn.click();
print(" Product added to the Cart successfully")
pr=driver.find_element(By.XPATH,"//div[@role='alert']").text
pr = pr.replace('View cart', '')
P_rate =driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/main/div[2]/div[2]/p/ins/span/bdi").text
P_rate=P_rate.replace('$', '')
print("Product price = "+P_rate);
time.sleep(3)

driver.execute_script("window.open('about:blank','tab2');")
driver.switch_to.window("tab2")      
driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/checkout")
driver.implicitly_wait(30)
driver.find_element(By.ID,"billing_first_name").send_keys("Fname")
driver.find_element(By.ID,"billing_last_name").send_keys("Lname")
        
country= Select(driver.find_element(By.ID,"billing_country"))
country.select_by_value("IN")
        
driver.find_element(By.ID,"billing_address_1").send_keys("123 abc")
driver.find_element(By.ID,"billing_city").send_keys("Calicut")

state_kerala= Select(driver.find_element(By.ID,"billing_state"))
state_kerala.select_by_value("KL")
driver.find_element(By.ID,"billing_postcode").send_keys("673016")
driver.find_element(By.ID,"billing_phone").send_keys("9876543210")
driver.find_element(By.ID,"billing_email").send_keys("mufidauc@gmail.com")
driver.find_element(By.ID,"need_delivery_yes").click()
Expected_Price= 40.00 + float(P_rate)
Expected_Price='%.2f'%Expected_Price
print("Expected Product Price = "+str(Expected_Price))
Actprice= driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/main/article/div/div/form[2]/div[2]/table/tfoot/tr[4]/td/strong/span/bdi")
driver.execute_script("arguments[0].scrollIntoView();", Actprice)
Actvalue=Actprice.text
# print("Actual price= "+ Actvalue)
Actual_rate=Actvalue.replace("$", "")
print("Actual_rate=" + Actual_rate)
if Actual_rate == Expected_Price:
    print("The product price has displayed correctly on the order summary page")
else :
    print("Actual product price displayed on order summary does not match with expected price ")
         
driver.find_element(By.ID,"delivery_date").click()
driver.find_element(By.XPATH,"/html/body/div[4]/table/tbody/tr[5]/td[2]/a").click()
driver.find_element(By.ID,"delivery_time").click()
driver.find_element(By.XPATH,"/html/body/div[5]/ul/li[23]").click()
driver.find_element(By.ID,"delivery_addons_packing").click()
driver.find_element(By.ID,"delivery_addons_wooden_box").click()
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/main/article/div/div/form[2]/div[2]/div/ul/li[3]/label')))
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/main/article/div/div/form[2]/div[2]/div/ul/li[3]/label").click()
driver.find_element(By.ID,"place_order").click()
print("=== SUCCESSFULLY PLACED THE ORDER ===")

# driver.quit()

