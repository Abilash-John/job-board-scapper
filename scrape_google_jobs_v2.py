from selenium import webdriver
import time
import openpyxl
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Replace with the path to your chromedriver executable
driver = webdriver.Chrome()
# chrome_driver_path = '/path/to/chromedriver'
# Create a new instance of the Chrome driver
# driver = webdriver.Chrome()
# URL to open
url = 'https://www.google.com/search?q=google+jobs&sxsrf=AB5stBjO706XYshQnGaorgMzHM9RXn-N_A:1691103714334&source=hp&ei=4jHMZJGwEuzO2roP0uK0mAo&iflsig=AD69kcEAAAAAZMw_8pht70ynEp-sqbmIE9FL-Oh5ixqD&oq=goo&gs_lp=Egdnd3Mtd2l6GgIYAyIDZ29vKgIIADIHECMYigUYJzILEAAYigUYkQIYiwMyERAuGIAEGLEDGIMBGMcBGNEDMg4QABiABBixAxiDARiLAzIOEAAYgAQYsQMYgwEYiwMyDhAAGIAEGLEDGIMBGIsDMg4QABiABBixAxiDARiLAzIUEC4YgAQYsQMYgwEYiwMYqAMYmAMyDhAAGIAEGLEDGIMBGIsDMhEQABiABBixAxiDARjJAxiLA0iIFFCMAlikBXABeACQAQCYAWigAbICqgEDMS4yuAEDyAEA-AEBqAIKwgIHECMY6gIYJ8ICCBAAGIoFGJECwgIaEC4YgAQYsQMYgwEYxwEY0QMYiwMYqAMY0gPCAggQABiABBiLAw&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwjvoM-jzMGAAxWqbmwGHV2yC2kQutcGKAF6BAhBEAY#htivrt=jobs&htidocid=vNNS12s5O0IAAAAAAAAAAA%3D%3D&fpstate=tldetail'

# Open the URL in the browser
driver.get(url)
time.sleep(5)
#div_element = driver.find_element_by_class_name('PUpOsf')
#div_text = div_element.text
#print("Data from the div:")
#print(div_text)

 # div_element1 = driver.find_element(By.CLASS_NAME, "BjJfJf.PUpOsf")

 # div_element2 = driver.find_element(By.CLASS_NAME, "vNEEBe")
 # div_element3 = driver.find_element(By.CLASS_NAME, "Qk80Jf")
 # div_element4 = driver.find_element(By.CLASS_NAME, "Qk80Jf")
 # div_element5 = driver.find_element(By.CLASS_NAME, "LL4CDc")
 # Get text of div element
 # div_text1 = div_element1.text

 # div_text2 = div_element2.text
 # div_text3 = div_element3.text
 # div_text4 = div_element4.text
 # div_text5 = div_element5.text
 # print(div_text1)

 # print(div_text2)
 # print(div_text3)
 # print(div_text4)
 # print(div_text5)

 # div_elements = driver.find_elements(By.TAG_NAME, "div")
 # for index, div in enumerate(div_elements):
 #    print(f'Div Element {index+1}\n{div.text}\n') "//*[@id='child2']/following-sibling::*
 # childrenlist = driver.find_elements(By.XPATH, "//*[@class='oNwCmf']/*")

try:
 jobtitle = driver.find_elements(By.XPATH,"//*[@class='mVlBke']/following-sibling::*")
 company = driver.find_elements(By.CLASS_NAME, 'vNEEBe')
 location_platform = driver.find_elements(By.CLASS_NAME, 'Qk80Jf')
 posted_time = driver.find_elements(By.CSS_SELECTOR, 'span.LL4CDc')

 try:
   for job in jobtitle:print(job.text)
    # for comp in company:

     # print(comp.text)
     # for location in location_platform:
     #  print(location.get_attribute("innerHTML"))


      # for time in posted_time:
      #  print(time.get_attribute("innerHTML"))
 except Exception as e:
    print("An error occurred:", e)

except NoSuchElementException:
    print("The div element does not exist.")

    # Display the next 5 texts from the second_list
    # for children in childrenlist[:5]:
    #     # Display the current second_text
    #     print("Second Text:", children.text)
    # childrenlist = childrenlist[5:]
    #



 # location = driver.find_element(By.CLASS_NAME, 'Qk80Jf')
#  # platform = driver.find_element(By.NAME, 'via')
#  # posted_on = driver.find_element(By.CLASS_NAME, 'LL4CDc')
#
#  print(company.get_attribute("outerHTML"))
# for location in location_platform:
#     print(location.get_attribute("outerHTML"))
#  # for job in jobtitle:
 #   print(job.text)
 #   for children in childrenlist:
 #    print(children.text)




    # workbook = openpyxl.load_workbook("Excel.xlsx")
    # sheet = workbook['LoginTest']
    # sheet.cell(row=2,column=1).value=(job.text)
    #
    # workbook.save("Excel.xlsx")





 # childrenlist = driver.find_elements(By.XPATH, "//*[@class='oNwCmf']/*")
 # for children in childrenlist:
 #            print(children.text)

 # print(children)

