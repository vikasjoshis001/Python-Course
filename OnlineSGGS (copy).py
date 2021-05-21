from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/home/vikasjoshis001/chromedriver')

# print("Enter your Registration Number :-\n")
reg = "2019bcs140"

driver.get("https://onlinesggs.org/app/web/index.php")

username = driver.find_element_by_name("mobile")
username.clear()
username.send_keys(reg+"@sggs.ac.in")

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(reg)

driver.find_element_by_name("sub").click()

status = driver.find_element_by_name("status")
status.send_keys("Regular")

year = driver.find_element_by_name("year")
year.send_keys("F.Y. SEM1")

driver.find_element_by_name("submit").click()