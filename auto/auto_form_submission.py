import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import xlrd
options = Options()


options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get('http://localhost:8000/')
df = pd.read_excel('media/covid_tests.xlsx')
dataindex = df.index
for i in dataindex:
    test = df.loc[i]


    patient_name = browser.find_element(By.NAME, "patient_name")
    patient_name.send_keys(test['name'])

    test_result = browser.find_element(By.XPATH, "//select[@name='test_result']")
    test_result.send_keys(test['test_result'])


    gender = browser.find_element(By.XPATH, f"//input[@name='gender'][@value='{test['gender']}']")
    gender.click()
    
    all_symptoms = test['symptoms']
    each_symp = all_symptoms.split(', ')
    for i in each_symp:
        print(i)
        symptoms = browser.find_element(By.XPATH, f"//input[@type='checkbox'][@value='{i}']")
        symptoms.click()  
        
    save_btn = browser.find_element(By.CLASS_NAME, "btn-submit")
    save_btn.click()
    time.sleep(5)


