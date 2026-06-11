import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Create a Chrome WebDriver instance
driver: webdriver = webdriver.Chrome()

# Navigate to the Google search results page for data scientist jobs in Newport Beach, California
driver.get("https://www.google.com/search?q=data+scientist+jobs+in+newport+beach+california&rlz=1C5CHFA_enIN1018IN1018&oq=data+scientist+jobs+in+newport+beach+california&aqs=chrome..69i57j0i546l5.29241j0j7&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwiem-GSzuD9AhWlRWwGHf4BDUEQutcGKAF6BAgLEAU#htivrt=jobs&htidocid=oNLz_cZbEd0AAAAAAAAAAA%3D%3D&fpstate=tldetail")

# Define XPath expressions for different pieces of information
xpaths = {
    'Logo': "./div[1]//img",
    'Role': "./div[2]",
    'Company': "./div[4]/div/div[1]",
    'Location': "./div[4]/div/div[2]",
    'Source': "./div[4]/div/div[3]",
    'Posted': ".//*[name()='path'][contains(@d,'M11.99')]/ancestor::div[1]",
    'Full / Part Time': ".//*[name()='path'][contains(@d,'M20 6')]/ancestor::div[1]",
    'Salary': ".//*[name()='path'][@fill-rule='evenodd']/ancestor::div[1]"
}

# Create an empty dictionary to store extracted data
data = {key: [] for key in xpaths}

# Initialize variables for tracking jobs
jobs_done = 0

# Scroll down repeatedly to load all job listings
while True:
    # Find all job listing elements using the defined XPath
    lis = driver.find_elements(By.XPATH, "//li[@data-ved]//div[@role='treeitem']/div/div")

    # Break the loop if all job listings have been processed
    if jobs_done >= len(lis):
        break

    # Iterate through each job listing element
    for li in lis[jobs_done:]:
        # Scroll the page to bring the current element into view
        driver.execute_script('arguments[0].scrollIntoView({block: "center", behavior: "smooth"});', li)

        # Iterate through the defined XPath keys to extract information in the specified order
        for key in ['Logo', 'Role', 'Company', 'Location', 'Source', 'Posted', 'Full / Part Time', 'Salary']:
            try:
                # Extract data from the current job listing using the XPath
                t = li.find_element("xpath", xpaths[key]).get_attribute('src' if key == 'Logo' else 'innerText')
            except NoSuchElementException:
                # Handle missing data by assigning a placeholder
                t = '*missing data*'
            
            # Append the extracted data to the corresponding list in the 'data' dictionary
            data[key].append(t)

        # Increment the counter for processed jobs and print progress
        jobs_done += 1
        print(f'{jobs_done=}', end='\r')
        
        # Introduce a short delay before processing the next listing
        time.sleep(.2)

# Print the extracted information for each job listing
for i in range(len(data['Role'])):
    print(f"Logo: {data['Logo'][i]}")
    print(f"Role: {data['Role'][i]}")
    print(f"Company: {data['Company'][i]}")
    print(f"Location: {data['Location'][i]}")
    print(f"Source: {data['Source'][i]}")
    print(f"Posted: {data['Posted'][i]}")
    print(f"Full / Part Time: {data['Full / Part Time'][i]}")
    print(f"Salary: {data['Salary'][i]}")
    print("=" * 50)

# Close the WebDriver
driver.quit()
