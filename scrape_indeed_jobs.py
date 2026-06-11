import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: WebDriver = webdriver.Chrome()
driver.get("https://in.indeed.com/jobs?q=product+manager&l=Bangalore%2C+Karnataka&vjk=82c98bcd45739295&advn=9740249730601869")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='css-tvvxwd ecydgvn1']/button[text()='1']").click()
time.sleep(3)

total_jobs = driver.find_element(By.XPATH, "//div[@class='jobsearch-JobCountAndSortPane-jobCount css-1af0d6o eu4oa1w0']/span[1]").text
total_jobs = total_jobs.replace(",", "")
total_jobs = total_jobs.replace(" jobs", "")

page_size = 18

page_start = 1
page_end = int(total_jobs) // page_size

for page_num in range(page_start, page_end + 1):
    xpaths = {
        'Role': ".//td[@class='resultContent']/div[1]/h2/a/span",
        'Company': ".//td[@class='resultContent']/div[2]/div/span",
        'Location': ".//td[@class='resultContent']/div[2]/div/div",
        'Posted': ".//span[@class='date']",
        'Full / Part Time': ".//td[@class='resultContent']/div[3]/div[2]/div",
        'Salary': ".//td[@class='resultContent']/div[3]/div[1]/div"
    }

    data = {key: [] for key in xpaths}
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

        for key in ['Role', 'Company', 'Location', 'Posted', 'Full / Part Time', 'Salary']:
            try:
                element = li.find_element(By.XPATH, xpaths[key])
                t = element.text
            except NoSuchElementException:
                t = '*missing data*'
            data[key].append(t)

        jobs_done += 1
        time.sleep(.2)

    for i in range(len(data['Role'])):
        print(f"\nPage Number:{page_num} | Job Number: {i}")
        print(f"Role: {data['Role'][i]}")
        print(f"Company: {data['Company'][i]}")
        print(f"Location: {data['Location'][i]}")
        print(f"Posted: {data['Posted'][i]}")
        print(f"Full / Part Time: {data['Full / Part Time'][i]}")
        print(f"Salary: {data['Salary'][i]}")
        print("=" * 50)

    try:
        next_page_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='pagination-page-next']"))
        )
        next_page_link.click()
        time.sleep(5)

        # Check if the 'css-yi9ndv e8ju0x51' (pop-up skip) button is present and click it if found
        try:
            load_more_button = driver.find_element(By.CLASS_NAME, "css-yi9ndv.e8ju0x51")
            load_more_button.click()
            time.sleep(5)  # Adjust the sleep time if needed
        except NoSuchElementException:
            pass

    except TimeoutException:
        print("TimeoutException: Next page link not found")
        break

# Close the WebDriver
driver.quit()
