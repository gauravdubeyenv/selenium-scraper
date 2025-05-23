
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from openpyxl.utils import column_index_from_string
from datetime import datetime

# Auto-install ChromeDriver
chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Fixed scrape date
scrape_date = "2025-05-21"
excel_path = "test.xlsx"

# Load workbook and sheets
workbook = openpyxl.load_workbook(excel_path)
sheet_config = workbook["Config"]
sheet_link = workbook["Link"]

# Read configurations
configs = []
for row in sheet_config.iter_rows(min_row=2, values_only=True):
    site, station, analyzer, parameter, column_letter = row
    if all([site, station, analyzer, parameter, column_letter]):
        configs.append({
            "site": site.strip(),
            "station": station.strip(),
            "analyzer": str(analyzer).strip(),
            "parameter": parameter.strip(),
            "column": column_letter.strip()
        })

# Scraping logic (same as before)...
# [You can paste the rest of your scraping logic here]

# Save and close
workbook.save(excel_path)
driver.quit()
print("✅ All data written to Excel.")
