import requests
from selenium import webdriver
from selenium.webdriver.common.by import By



result = requests.get('https://www.googleapis.com/books/v1/volumes?q=user+story+mapping')
d1 = dict(result.json())
print(d1)
isbn10=[] # storing isbn of 10 digit format
isbn13=[] # storing isbn of 13 digit format

# Retrieving isbn from dictionary and storing it in respective lists
for i in range(11):
    try:
        a= d1['items'][i]['volumeInfo']['industryIdentifiers'][0]['identifier']
        b= d1['items'][i]['volumeInfo']['industryIdentifiers'][1]['identifier']
        if len(a) == 10:
            isbn10.append(a)
            isbn13.append(b)
        else:
            isbn10.append(b)
            isbn13.append(a)
    except:
        continue
print(isbn10)
print(isbn13)

chrome_options = webdriver.ChromeOptions()


driver = webdriver.Chrome(options=chrome_options)

wd = webdriver.Chrome('chromedriver')

# opening the website
wd.get('https://www.barnesandnoble.com/')

wd.implicitly_wait(10)

# sending random isbn to the search box
wd.find_element(By.XPATH, '//*[@id="rhf_header_element"]/nav/div/div[3]/form/div/div[2]/div/input[1]').send_keys(a)
wd.implicitly_wait(10)
wd.find_element(By.XPATH, '//*[@id="rhf_header_element"]/nav/div/div[3]/form/div/span/button').click()


#
# button = WebDriverWait(wd, 10).until(EC.element_to_be_clickable(wd.find_element(by=By.NAME, value='btnK')))
# button.click()



