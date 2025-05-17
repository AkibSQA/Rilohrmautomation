from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select





# Configure Chrome options
options = Options()
options.add_argument("--start-maximized")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# Step 1: Open the login page
driver.get("http://34.235.68.130:3000/auth/login")

# Step 2: Wait until username and password fields are present
wait = WebDriverWait(driver, 10)

# IMPORTANT: Replace these XPaths with actual ones if needed (non-standard characters may break)
username_xpath = '//*[@id="«R2sferb»-form-item"]'
password_xpath = '//*[@id="«R4sferb»-form-item"]'
login_button_xpath = '/html/body/div/div/div[2]/div/div[1]/div/form/button'

# Fill in login details
wait.until(EC.presence_of_element_located((By.XPATH, username_xpath))).send_keys("admin_rilohrm@yopmail.com")
wait.until(EC.presence_of_element_located((By.XPATH, password_xpath))).send_keys("123456")
wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()

# Step 3: Wait for login to process
time.sleep(5)

# Step 4: Navigate to Add Employee page
driver.get("http://34.235.68.130:3000/dashboard/employees/add-employee")

# Wait to confirm page load
time.sleep(5)


# Read Employment Info (Page 1)
first_name = "Anisur"
middle_name = "Rahman"
last_name = "Akib"
email = "akibsqae1234@gmail.com"
joining_date = "17/05/2025"
department = "Development"
designation = "SQA Engineer"
pay_type = "salary"
salary = "40000"
reporting_manager = "Mr Hr"
role = "Employee"
status = "active"
days = "3"
DOB = "11/06/1997"
phone = "01838792487"
name = "asif"
relation = "brother"
address = "Khulshi, Chittagong, GPO=4000 "
city = "Chittagong"
district = "Chittagong"
post_office = "Khulshi"
post_code = "4000"
country = "Bangladesh"

bank_name = "Dutch Bangla Bank"
branch = "Halishahar"
Ac = "1234567890"
Ac_name = "Anisur Rahman Akib"
route_no = "1234"
Tin = "123456"

wait.until(EC.presence_of_element_located(
    (By.XPATH, "//input[@placeholder='First name...']"))).send_keys(first_name)
driver.find_element(By.XPATH, "//input[@placeholder='Middle name...']").send_keys(middle_name)
driver.find_element(By.XPATH, "//input[@placeholder='Last name...']").send_keys(last_name)
driver.find_element(By.XPATH, "//input[@placeholder='Work email...']").send_keys(email)
driver.find_element(By.NAME, "joining_date").send_keys(joining_date)
driver.find_element(By.XPATH, "//input[@placeholder='Salary...']").send_keys(salary)
driver.find_element(By.ID, "checkbox-67f1fe44da294f1a41a71ab2").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Days...']").send_keys(days)

dropdown_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[span[text()='Select a designation']]")
))
dropdown_button.click()

# Step 2: Wait for the dropdown option 'designation' to appear and click it
option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='option' and normalize-space()='SQA Engineer']")
))
option.click()


dropdown_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[span[text()='Select a department']]")
))
dropdown_button.click()

# Step 2: Wait for the dropdown option 'designation' to appear and click it
option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='option' and normalize-space()='Development']")
))
option.click()


dropdown_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[span[text()='Select a pay type']]")
))
dropdown_button.click()

# Step 2: Wait for the dropdown option 'designation' to appear and click it
option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='option' and normalize-space()='salary']")
))
option.click()


#select role
dropdown_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[span[text()='Select a Role']]")
))
dropdown_button.click()

# Step 2: Wait for the dropdown option 'designation' to appear and click it
option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='option' and normalize-space()='employee']")
))
option.click()


#select status
dropdown_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[span[text()='Select a Status']]")
))
dropdown_button.click()

# Step 2: Wait for the dropdown option 'designation' to appear and click it
option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='option' and normalize-space()='active']")
))
option.click()

driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()\

time.sleep(10)

# SECOND PAGE START****************************

#select Gender
dropdown_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[span[text()='MALE']]")
))
dropdown_button.click()

# Step 2: Wait for the dropdown option 'designation' to appear and click it
option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='option' and normalize-space()='MALE']")
))
option.click()

#select Blood Group
dropdown_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[span[text()='A+']]")
))
dropdown_button.click()

# Step 2: Wait for the dropdown option 'designation' to appear and click it
option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='option' and normalize-space()='B+']")
))
option.click()

# DOB
driver.find_element(By.NAME, "date_of_birth").send_keys(DOB)

#email
driver.find_element(By.XPATH, "//input[@placeholder='Personal email...']").send_keys(email)
#phone
driver.find_element(By.XPATH, "//input[@placeholder='Phone...']").send_keys(phone)

#emergency
driver.find_element(By.XPATH, "//input[@placeholder='Name...']").send_keys(name)
driver.find_element(By.XPATH, "//input[@placeholder='Relation...']").send_keys(relation)

driver.find_element(By.XPATH, "//input[@placeholder='Phone number...']").send_keys(phone)

# driver.find_element(By.XPATH, "//input[@placeholder='Ex: Street name &amp; no, Apt or Suit no, City, State or District, P.O. name, Post Code and Country.']").send_keys(address)
address_field = driver.find_element(By.NAME, "emergency_contact_address")
address_field.send_keys(address)

driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()\

time.sleep(10)


# Third Page

driver.find_element(By.XPATH, "//input[@placeholder='Street name & no...']").send_keys(address)
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys(city)
driver.find_element(By.XPATH, "//input[@placeholder='District...']").send_keys(district)
driver.find_element(By.XPATH, "//input[@placeholder='Post office name...']").send_keys(post_office)
driver.find_element(By.XPATH, "//input[@placeholder='Post code...']").send_keys(post_code)
# driver.find_element(By.XPATH, "//input[@placeholder='Bangladesh...']").send_keys(country)
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()\


# Fourth Page
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()\

driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

# Step 1: Check for error and print if found
try:
    error_box = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "employeeForm_errorContainer__v7wrR")
    ))
    print("ERROR Happened ❌:")
    print(error_box.text.strip())
    print("Correcting Automatically")


    driver.find_element(By.XPATH, "//input[@placeholder='Street name & no...']").send_keys(address)
    driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys(city)
    driver.find_element(By.XPATH, "//input[@placeholder='District...']").send_keys(district)
    driver.find_element(By.XPATH, "//input[@placeholder='Post office...']").send_keys(post_office)
    driver.find_element(By.XPATH, "//input[@placeholder='Post code...']").send_keys(post_code)

    # Step 3: Click "Next" again
    driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

except:
    print("No error messages found. Likely passed validation.")



# Fifth Page


driver.find_element(By.XPATH, "//input[@placeholder='Bank name...']").send_keys(bank_name)
driver.find_element(By.XPATH, "//input[@placeholder='Branch name...']").send_keys(branch)
driver.find_element(By.XPATH, "//input[@placeholder='Account number...']").send_keys(Ac)
driver.find_element(By.XPATH, "//input[@placeholder='Account holder name...']").send_keys(Ac_name)
driver.find_element(By.XPATH, "//input[@placeholder='Routing number...']").send_keys(route_no)
driver.find_element(By.XPATH, "//input[@placeholder='TIN/SSN/SIN...']").send_keys(Tin)


driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()

time.sleep(10)

try:
    wait = WebDriverWait(driver, 10)
    toast = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//div[contains(@class, 'toast') or contains(@class, 'Toastify__toast')]"
    )))
    print("Toast Message:", toast.text.strip())
except:
    print("No toast message appeared.")


driver.get("http://34.235.68.130:3000/dashboard/employees")
time.sleep(12)
print("Redirected to the All Employees page successfully ✅")



time.sleep(120)

