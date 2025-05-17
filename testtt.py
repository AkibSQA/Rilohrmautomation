from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
import time

# Load Excel Data
wb = load_workbook(r"D:\Automation test\Rilohrm\dataentry.xlsx")
sheet = wb.active

def get_cell(cell):
    return str(sheet[cell].value).strip()

# Configure Chrome options
options = Options()
options.add_argument("--start-maximized")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# Step 1: Open the login page
driver.get("http://34.235.68.130:3000/auth/login")

# Step 2: Login to the system
username_xpath = '//*[@id="«R2sferb»-form-item"]'
password_xpath = '//*[@id="«R4sferb»-form-item"]'
login_button_xpath = '/html/body/div/div/div[2]/div/div[1]/div/form/button'

wait.until(EC.presence_of_element_located((By.XPATH, username_xpath))).send_keys("admin_rilohrm@yopmail.com")
wait.until(EC.presence_of_element_located((By.XPATH, password_xpath))).send_keys("123456")
wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()

# Step 3: Wait for login and navigate to Add Employee page
time.sleep(5)
driver.get("http://34.235.68.130:3000/dashboard/employees/add-employee")
time.sleep(5)

# Helper for selecting dropdown
def select_dropdown_value(button_id, value):
    driver.find_element(By.ID, button_id).click()
    option_xpath = f"//div[@role='option' and contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{value.lower()}')]"
    wait.until(EC.presence_of_element_located((By.XPATH, option_xpath))).click()

# -------------------------
# Step 1: Employment Info
# -------------------------
wait.until(EC.presence_of_element_located((By.ID, "«r57»-form-item"))).send_keys(get_cell("B2"))
driver.find_element(By.ID, "«r58»-form-item").send_keys(get_cell("B3"))
driver.find_element(By.ID, "«r59»-form-item").send_keys(get_cell("B4"))
driver.find_element(By.ID, "«r5a»-form-item").send_keys(get_cell("B5"))
driver.find_element(By.ID, "«r5b»-form-item").send_keys(get_cell("B6"))

select_dropdown_value("«r5c»-form-item", get_cell("B7"))
select_dropdown_value("«r5e»-form-item", get_cell("B8"))
select_dropdown_value("«r5g»-form-item", get_cell("B9"))
driver.find_element(By.ID, "«r5i»-form-item").send_keys(get_cell("B10"))
select_dropdown_value("«r5j»-form-item", get_cell("B11"))
select_dropdown_value("«r5n»-form-item", get_cell("B12"))
select_dropdown_value("«r5p»-form-item", get_cell("B13"))

driver.find_element(By.ID, "checkbox-67f1fe44da294f1a41a71ab2").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Days...']").send_keys(get_cell("B15"))

driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

# -------------------------
# Step 2: Personal Info
# -------------------------
upload_input = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='photo-upload']/following-sibling::input")))
upload_input.send_keys(r"D:\Automation test\Rilohrm\pppaakib.jpg")

select_dropdown_value("«r75»-form-item", get_cell("B19"))
select_dropdown_value("«r77»-form-item", get_cell("B20"))
driver.find_element(By.ID, "«r79»-form-item").send_keys(get_cell("B21"))
driver.find_element(By.ID, "«r7a»-form-item").send_keys(get_cell("B22"))
driver.find_element(By.ID, "«r7b»-form-item").send_keys(get_cell("B23"))

driver.find_element(By.ID, "«r7d»-form-item").send_keys(get_cell("B26"))
driver.find_element(By.ID, "«r7e»-form-item").send_keys(get_cell("B27"))
driver.find_element(By.ID, "«r7f»-form-item").send_keys(get_cell("B28"))
driver.find_element(By.ID, "«r7h»-form-item").send_keys(get_cell("B29"))

driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

# -------------------------
# Step 3: Present Address
# -------------------------
driver.find_element(By.ID, "«r7s»-form-item").send_keys(get_cell("B33"))
driver.find_element(By.ID, "«r7u»-form-item").send_keys(get_cell("B34"))
driver.find_element(By.ID, "«r7v»-form-item").send_keys(get_cell("B35"))
driver.find_element(By.ID, "«r80»-form-item").send_keys(get_cell("B36"))
driver.find_element(By.ID, "«r81»-form-item").send_keys(get_cell("B37"))
driver.find_element(By.ID, "«r82»-form-item").send_keys(get_cell("B38"))

driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

# -------------------------
# Step 4: Permanent Address
# -------------------------
driver.find_element(By.ID, "«r83»-form-item").send_keys(get_cell("B42"))
driver.find_element(By.ID, "«r85»-form-item").send_keys(get_cell("B43"))
driver.find_element(By.ID, "«r86»-form-item").send_keys(get_cell("B44"))
driver.find_element(By.ID, "«r87»-form-item").send_keys(get_cell("B45"))
driver.find_element(By.ID, "«r88»-form-item").send_keys(get_cell("B46"))
driver.find_element(By.ID, "«r89»-form-item").send_keys(get_cell("B47"))

driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

# -------------------------
# Final Submit
# -------------------------
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

# Optional: wait before closing
time.sleep(5)
driver.quit()