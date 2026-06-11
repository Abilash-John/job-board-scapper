import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

excel_file_path = "C:\\Users\\Abilash\\Downloads\\Emails to Verify Format.xlsx"
workbook = openpyxl.load_workbook(excel_file_path)

# Select the first sheet (by index)
sheet = workbook.worksheets[0]

# Fetch data from the first column
first_column_data = [cell.value for cell in sheet['A']]

driver = webdriver.Chrome()

# Loop through each data in the list
for data in first_column_data:
    print(f"\nMail id : {data}")
    # Open a website using Selenium (Replace with the URL you want to open)
    website_url = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AXo7B7VPsp73NQfv9I5vAsHy_JC0ozdTQ3tVoeEwVjzzY2956RN5Tx8C3yXDMCSQeoiMcvY8hRgw&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S100876893%3A1692880188077944'
    driver.get(website_url)

    search_box = driver.find_element(By.XPATH, '//div[@class="Xb9hP"]/input')
    search_box.clear()
    search_box.send_keys(data)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    error_gmail = "Couldn’t find your Google Account"
    error_outlook = "get a new one"

    try:
        check = driver.find_element(By.XPATH, '//div[@class="o6cuMc Jj6Lae"]')
        if check.text == error_gmail:
            # Gmail doesn't exist
            website_url = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=16&ct=1692884976&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dce82b497-4a23-216f-dfd4-60e4dbcd0602&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015'
            driver.get(website_url)

            input_box = driver.find_element(By.XPATH, '//div[@class="placeholderContainer"]/input[@type="email"]')
            input_box.clear()
            input_box.send_keys(data)
            input_box.send_keys(Keys.RETURN)
            time.sleep(5)

            try:
                error_check = driver.find_element(By.XPATH, '//div[@id="usernameError"]/a[@id="idA_PWD_SignUp"]')
                if error_check.text == error_outlook:
                    print("Mail id doesn't exist")
                else:
                    print("Outlook account")
            except NoSuchElementException:
                print("Outlook account")
        else:
            print("Gmail account")
    except NoSuchElementException:
        print("Gmail account")

    # Wait for a while to see the result (you can adjust the sleep time)
    time.sleep(5)

# Close the Selenium webdriver
driver.quit()
