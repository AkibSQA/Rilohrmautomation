import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook

# === Step 1: Read Username & Password from Excel ===
excel_path = r"D:\Automation test\Rilohrm\automationtest.xlsx"

# Load workbook and sheet
wb = load_workbook(excel_path)
sheet = wb.active

# Read credentials
username = sheet["A2"].value
password = sheet["B2"].value

# === Step 2: Launch browser and open login page ===
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://34.235.68.130:3000/auth/login")

# === Step 3: Perform login ===
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="«R2sferb»-form-item"]'))
    )

    driver.find_element(By.XPATH, '//*[@id="«R2sferb»-form-item"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="«R4sferb»-form-item"]').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div/form/button').click()

except Exception as e:
    print("Error during login input:", e)
    sheet["D2"] = f"❌ Error during login input: {e}"
    sheet["E2"] = "Fail"
    wb.save(excel_path)
    driver.quit()
    exit()

# === Step 4: Optional - Capture toaster message ===
try:
    toast_container = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Toastify"))
    )
    print("Toaster Message:", toast_container.text)
except:
    print("No toaster message found.")

# === Step 5: Verify dashboard element and write result back to Excel ===
try:
    dashboard_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[2]/ul/li[1]/span/a'))
    )
    result = "✅ Login successful. Dashboard is visible."
    print(result)
    sheet["D2"] = result
    sheet["E2"] = "Pass"

except:
    result = "❌ Login failed. Dashboard not found."
    print(result)
    sheet["D2"] = result
    sheet["E2"] = "Fail"

time.sleep(10)

# === Step 6: Navigate to Employees Page ===
# === Navigate to Employees Page and Print Result ===
try:
    driver.get("http://34.235.68.130:3000/dashboard/employees")


    result = "✅ Navigated to Employees page successfully."
    print(result)
    sheet["D3"] = result  # L
    sheet["E3"] = "Pass"

except Exception as e:
    result = f"❌ Failed to navigate to Employees page: {e}"
    print(result)
    sheet["D3"] = result
    sheet["E3"] = "Fail"

wb.save(excel_path)
time.sleep(3)
time.sleep(999999)
