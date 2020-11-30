import threading
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException, \
    NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask
from Query_Modification import NLP
from Extracting_Deep_Web import SearchableDatabase
from Extracting_Deep_Web import ClassifyForm
from User_Query import UserQuery
from Extracting_Deep_Web import DataCrawal

app = Flask(__name__)


@app.route('/run', methods=['GET', 'POST'])
def my_function():
    #E:\chromedriver_win32
    driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.google.com")

    dataCrawler= DataCrawal.datacrawal()
    dataCrawler.startCroawler(driver)


if __name__ == '__main__':
    app.run(debug=True)