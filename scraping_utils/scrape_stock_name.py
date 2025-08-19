from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import os


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.nepalstock.com/company")
time.sleep(2)
sector_dropdown = Select(driver.find_element(
    By.XPATH,
    "//select[option[contains(text(), 'Hydro Power')]]"
))

sector_dropdown.select_by_visible_text("Hydro Power")
items_per_page = Select(driver.find_element(
    By.XPATH,
    "//select[option[contains(text(), '200')]]"
))
items_per_page.select_by_visible_text('200')

driver.find_element(By.CLASS_NAME, 'box__filter--search').click()
time.sleep(1)

table = driver.find_element(
    By.CSS_SELECTOR,
    "div.table-responsive > table"
)

rows = table.find_elements(
    By.CSS_SELECTOR, "tbody tr"
)

data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    data.append(cols[2].text)

dataSeries = pd.Series(data, name='Symbol')
file_path = os.path.abspath(os.path.join('..', 'stock_name_data', 'hydropower.csv'))
dataSeries.to_csv(file_path, index=False)
driver.close()