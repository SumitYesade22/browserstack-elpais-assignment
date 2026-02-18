from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://elpais.com/opinion/")

input("Press Enter to close browser...")
driver.quit()
