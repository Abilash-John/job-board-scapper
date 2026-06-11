# # import time
# # import random
# # from selenium import webdriver
# # from selenium.webdriver.chrome.webdriver import WebDriver
# # from selenium.webdriver.common.by import By
# # from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # driver: WebDriver = webdriver.Chrome()
# # time.sleep(5)
# # driver.get("https://in.indeed.com/jobs?q=product+manager&l=Bangalore%2C+Karnataka&vjk=82c98bcd45739295&advn=9740249730601869")
# # time.sleep(25)
# #
# # # checkbox_xpath = "//input[type='checkbox']"
# # # def check_checkbox(driver, checkbox_xpath):
# # #     try:
# # #         checkbox = driver.find_element(By.XPATH, checkbox_xpath)
# # #         if checkbox.get_attribute("type") == "checkbox":
# # #             if not checkbox.is_selected():
# # #                 checkbox.click()
# # #     except Exception as e:
# # #         pass
# #
# # driver.maximize_window()
# #
# # total_jobs_element = driver.find_element(By.XPATH, "//div[@class='jobsearch-JobCountAndSortPane-jobCount css-1af0d6o eu4oa1w0']/span[1]")
# # total_jobs = int(total_jobs_element.text.replace(",", "").replace(" jobs", ""))
# # page_size = 18
# # page_end = total_jobs // page_size + 1
# #
# # for page_num in range(1, page_end + 1):
# #     xpaths = {
# #         'Role': ".//td[@class='resultContent']/div[1]/h2/a/span",
# #         'Company': ".//td[@class='resultContent']/div[2]/div/span",
# #         'Location': ".//td[@class='resultContent']/div[2]/div/div",
# #         'Posted': ".//span[@class='date']",
# #         'Full / Part Time': ".//td[@class='resultContent']/div[3]/div[2]/div",
# #         'Salary': ".//td[@class='resultContent']/div[3]/div[1]/div"
# #     }
# #
# #     data = {key: [] for key in xpaths}
# #
# #     jobs_done = 0
# #
# #     while True:
# #         lis = driver.find_elements(By.XPATH, "//*[@id='mosaic-provider-jobcards']/ul/li")
# #
# #         if jobs_done >= len(lis):
# #             break
# #         for job_num in range(len(lis)):
# #             li = lis[jobs_done]  # Get the current list item
# #
# #             # --- Skip non-job content
# #             if li.find_elements(By.CLASS_NAME, "mosaic-zone.nonJobContent-desktop"):
# #                 jobs_done += 1
# #                 continue
# #             # ---
# #
# #             try:
# #                 li.click()  # Click on the job list item to access job description
# #                 WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//div[@id='jobDescriptionText']")))
# #                 sleep_time = random.uniform(5, 10)
# #                 time.sleep(sleep_time)
# #
# #                 job_description_element = driver.find_element(By.XPATH, ".//div[@id='jobDescriptionText']")
# #                 job_description = job_description_element.text
# #
# #                 company_website_element = driver.find_element(By.XPATH, ".//a[@class='css-1f8zkg3 e19afand0']")
# #                 company_website = company_website_element.get_attribute("href")
# #
# #                 # Open the company website in a new window
# #                 driver.execute_script(f"window.open('{company_website}', '_blank');")
# #                 # Switch to the new window
# #                 driver.switch_to.window(driver.window_handles[-1])
# #
# #                 try:
# #                     # Extract company size information from the new window
# #                     company_size_element = driver.find_element(By.XPATH, ".//div[@class='css-1k40ovh e1wnkr790']")
# #                     company_size = company_size_element.text
# #                 except NoSuchElementException:
# #                     company_size = '*missing company size*'
# #
# #                 # Close the new window
# #                 driver.close()
# #                 # Switch back to the original window
# #                 driver.switch_to.window(driver.window_handles[0])
# #
# #             except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
# #                 job_description = '*missing job description*'
# #                 company_website = '*missing company website*'
# #                 company_size = '*missing company size*'
# #
# #         for key, xpath in xpaths.items():
# #             try:
# #                 element = li.find_element(By.XPATH, xpath)
# #                 t = element.text
# #             except NoSuchElementException:
# #                 t = '*missing data*'
# #             data[key].append(t)
# #         for i in range(len(data['Role'])):
# #             print(f"\nPage Number: {page_num} | Job Number: {i}")
# #             print(f"Role: {data['Role'][i]}")
# #             print(f"Company: {data['Company'][i]}")
# #             print(f"Location: {data['Location'][i]}")
# #             print(f"Posted: {data['Posted'][i]}")
# #             print(f"Full / Part Time: {data['Full / Part Time'][i]}")
# #             print(f"Salary: {data['Salary'][i]}")
# #             print(f"Company Website: {company_website}")
# #             print(f"Company Size: {company_size}")
# #             print(f"Job Description: {job_description}")
# #             print("=" * 50)
# #
# #         jobs_done += 1
# #
# #     # Go to the next page
# #     try:
# #         next_page_link = WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='pagination-page-next']"))
# #         )
# #         next_page_link.click()
# #         time.sleep(5)
# #         try:
# #             load_more_button = driver.find_element(By.CLASS_NAME, "css-yi9ndv.e8ju0x51")
# #             load_more_button.click()
# #             time.sleep(5)  # Adjust the sleep time if needed
# #         except NoSuchElementException:
# #             pass
# #     except TimeoutException:
# #         print("TimeoutException: Next page link not found")
# #         break
# #
# # # Close the WebDriver
# # driver.quit()
# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver: WebDriver = webdriver.Chrome()
# time.sleep(5)
# driver.get("https://in.indeed.com/jobs?q=product+manager&l=Bangalore%2C+Karnataka&vjk=82c98bcd45739295&advn=9740249730601869")
# time.sleep(25)
#
# driver.maximize_window()
#
# total_jobs_element = driver.find_element(By.XPATH, "//div[@class='jobsearch-JobCountAndSortPane-jobCount css-1af0d6o eu4oa1w0']/span[1]")
# total_jobs = int(total_jobs_element.text.replace(",", "").replace(" jobs", ""))
# page_size = 18
# page_end = total_jobs // page_size + 1
#
# for page_num in range(1, page_end + 1):
#     xpaths = {
#         'Role': ".//td[@class='resultContent']/div[1]/h2/a/span",
#         'Company': ".//td[@class='resultContent']/div[2]/div/span",
#         'Location': ".//td[@class='resultContent']/div[2]/div/div",
#         'Posted': ".//span[@class='date']",
#         'Full / Part Time': ".//td[@class='resultContent']/div[3]/div[2]/div",
#         'Salary': ".//td[@class='resultContent']/div[3]/div[1]/div"
#     }
#
#     jobs_done = 0
#
#     while True:
#         lis = driver.find_elements(By.XPATH, "//*[@id='mosaic-provider-jobcards']/ul/li")
#
#         if jobs_done >= len(lis):
#             break
#
#         li = lis[jobs_done]  # Get the current list item
#
#         # --- Skip non-job content
#         if li.find_elements(By.CLASS_NAME, "mosaic-zone.nonJobContent-desktop"):
#             jobs_done += 1
#             continue
#         # ---
#
#         try:
#             li.click()  # Click on the job list item to access job description
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//div[@id='jobDescriptionText']")))
#             sleep_time = random.uniform(5, 10)
#             time.sleep(sleep_time)
#
#             job_description_element = driver.find_element(By.XPATH, ".//div[@id='jobDescriptionText']")
#             job_description = job_description_element.text
#
#             company_website_element = driver.find_element(By.XPATH, ".//a[@class='css-1f8zkg3 e19afand0']")
#             company_website = company_website_element.get_attribute("href")
#
#             try:
#                 company_size_element = driver.find_element(By.XPATH, ".//div[@class='css-1k40ovh e1wnkr790']")
#                 company_size = company_size_element.text
#             except NoSuchElementException:
#                 company_size = '*missing company size*'
#
#         except (NoSuchElementException, TimeoutException, ElementNotInteractableException):
#             job_description = '*missing job description*'
#             company_website = '*missing company website*'
#             company_size = '*missing company size*'
#
#         role = li.find_element(By.XPATH, xpaths['Role']).text
#         company = li.find_element(By.XPATH, xpaths['Company']).text
#         location = li.find_element(By.XPATH, xpaths['Location']).text
#         posted = li.find_element(By.XPATH, xpaths['Posted']).text
#         full_part_time = li.find_element(By.XPATH, xpaths['Full / Part Time']).text
#         salary = li.find_element(By.XPATH, xpaths['Salary']).text
#
#         print(f"\nPage Number: {page_num} | Job Number: {jobs_done}")
#         print(f"Role: {role}")
#         print(f"Company: {company}")
#         print(f"Location: {location}")
#         print(f"Posted: {posted}")
#         print(f"Full / Part Time: {full_part_time}")
#         print(f"Salary: {salary}")
#         print(f"Company Website: {company_website}")
#         print(f"Company Size: {company_size}")
#         print(f"Job Description: {job_description}")
#         print("=" * 50)
#
#         jobs_done += 1
#         try:
#             next_page_link = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='pagination-page-next']"))
#             )
#             next_page_link.click()
#             time.sleep(5)
#             try:
#                 load_more_button = driver.find_element(By.CLASS_NAME, "css-yi9ndv.e8ju0x51")
#                 load_more_button.click()
#                 time.sleep(5)  # Adjust the sleep time if needed
#             except NoSuchElementException:
#                  pass
#         except TimeoutException:
#             print("TimeoutException: Next page link not found")
#         break
#
#
# driver.quit()
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_job_data(li):
    xpaths = {
        'Role': ".//h2/a/span",
        'Company': ".//div[@class='company']/span",
        'Location': ".//div[@class='location accessible-contrast-color-location']",
        'Posted': ".//span[@class='date date-a11y']",
        'Full / Part Time': ".//div[@class='jobsearch-JobMetadataFooter']",
        'Salary': ".//span[@class='salaryText']",
        'Job description': ".//div[@id='jobDescriptionText']"
    }

    data = {key: '*missing data*' for key in xpaths}

    for key, xpath in xpaths.items():
        try:
            element = li.find_element(By.XPATH, xpath)
            t = element.text
            data[key] = t
        except NoSuchElementException:
            pass

    return data

driver: WebDriver = webdriver.Chrome()
time.sleep(5)
driver.get("https://in.indeed.com/jobs?q=product+manager&l=Bangalore%2C+Karnataka&vjk=82c98bcd45739295&advn=9740249730601869")
time.sleep(25)

driver.maximize_window()

page_start = 1
total_jobs_element = driver.find_element(By.XPATH, "//div[@class='jobsearch-JobCountAndSortPane-jobCount css-1af0d6o eu4oa1w0']/span[1]")
total_jobs = int(total_jobs_element.text.replace(",", "").replace(" jobs", ""))
page_size = 18
page_end = total_jobs // page_size + 1

for page_num in range(page_start, page_end + 1):
    jobs_done = 0

    while True:
        lis = driver.find_elements(By.XPATH, "//*[@id='mosaic-provider-jobcards']/ul/li")

        if jobs_done >= len(lis):
            break

        li = lis[jobs_done]  # Get the current list item

        # Check if the current list item contains mosaic content, skip if it does
        if li.find_elements(By.CLASS_NAME, "mosaic-zone.nonJobContent-desktop"):
            jobs_done += 1
            continue

        try:
            li.click()  # Click on the job list item to access job description
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//div[@id='jobDescriptionText']")))
            time.sleep(5)  # Let the page load completely

            job_data = extract_job_data(li)

            # Extract job description from the expanded view
            job_description_element = driver.find_element(By.XPATH, ".//div[@id='jobDescriptionText']")
            job_data['Job description'] = job_description_element.text

            # Print job data
            print(f"\nPage Number: {page_num} | Job Number: {jobs_done}")
            for key, value in job_data.items():
                print(f"{key}: {value}")
            print("=" * 50)

            jobs_done += 1
            time.sleep(2)  # Introducing a small delay between job listings

        except (NoSuchElementException, TimeoutException):
            jobs_done += 1
            pass

    # Go to the next page
    try:
        next_page_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='pagination-page-next']"))
        )
        next_page_link.click()
        time.sleep(5)

    except TimeoutException:
        print("TimeoutException: Next page link not found")
        break

# Close the WebDriver
driver.quit()
