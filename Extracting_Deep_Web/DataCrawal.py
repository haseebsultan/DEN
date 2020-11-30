import threading
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException, \
    NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Query_Modification import NLP
from Extracting_Deep_Web import SearchableDatabase
from Extracting_Deep_Web import ClassifyForm
from User_Query import UserQuery

class datacrawal:

    def startCroawler(self, driver):
        elem = ""
        find = 0
        while (1):
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.new_window_is_opened(driver.window_handles))
            except Exception as e:
                element = e
            finally:
                try:
                    element = driver.find_element_by_css_selector("input[class='gLFyf gsfi']")
                    value1 = element.get_attribute("value")
                    searchabledatabase = SearchableDatabase.SearchableDatabase.getInstance()
                    userquery = UserQuery.user_query()
                    userquery.setUserQuery(value1)
                    classifyform = ClassifyForm.classifyform()
                    nlp = userquery.getNLP()
                    print(len(value1))
                    print("jiji" + value1)
                    if len(value1) > 0:
                        nlp.apply_nlp2(searchabledatabase, userquery.getUserQuery())

                except Exception as e:
                    elem = e
                finally:
                    try:
                        if (find == 0):
                            elem = driver.find_element_by_id(classifyform.getTextBoxId_3())
                            value = elem.get_attribute("value")


                            a = len(value)
                            if (len(value) == 0):
                                find = 0
                                print("I am in PakWheel")
                                text_area2 = driver.find_element_by_class_name("pr35")
                                tempvalue = text_area2.get_attribute("value")
                                if len(tempvalue) == 0:
                                    text_area2.send_keys(searchabledatabase.get_company_name())
                                    element = driver.find_element_by_css_selector(
                                        "input[class='btn btn-primary refine-go']")
                                    element.click()

                                if searchabledatabase.getrangeValue_1() != "":
                                    if searchabledatabase.getrangeValue_2() != "":

                                        elem = driver.find_element_by_name(classifyform.getTextBoxId_2())
                                        tempvalue1 = elem.get_attribute("value")
                                        if len(tempvalue1) == 0:
                                            elem.send_keys(searchabledatabase.getrangeValue_1())

                                        elem = driver.find_element_by_name(classifyform.getTextBoxId_3())
                                        tempvalue2 = elem.get_attribute("value")
                                        if len(tempvalue2) == 0:
                                            elem.send_keys(searchabledatabase.getrangeValue_2())

                                        text_area = driver.find_element_by_id("pr-go")
                                        text_area.click()
                                    else:
                                        elem = driver.find_element_by_name(classifyform.getTextBoxId_2())
                                        tempvalue3 = elem.get_attribute("value")
                                        if len(tempvalue3) == 0:
                                            elem.send_keys(searchabledatabase.getrangeValue_1())
                                            text_area = driver.find_element_by_id("pr-go")
                                            text_area.click()

                                time.sleep(4)

                                if searchabledatabase.getrangeYear_1() != "":
                                    if searchabledatabase.getrangeYear_2() != "":
                                        elem = driver.find_element_by_name(classifyform.getTextBoxId_4())
                                        tempvalue4 = elem.get_attribute("value")
                                        if len(tempvalue4) == 0:
                                            elem.send_keys(searchabledatabase.getrangeYear_1())

                                        elem = driver.find_element_by_name(classifyform.getTextBoxId_5())
                                        tempvalue5 = elem.get_attribute("value")
                                        if len(tempvalue5) == 0:
                                            elem.send_keys(searchabledatabase.getrangeYear_2())

                                        text_area = driver.find_element_by_id("yr-go")
                                        text_area.click()
                                    else:
                                        elem = driver.find_element_by_name(classifyform.getTextBoxId_4())
                                        tempvalue6 = elem.get_attribute("value")
                                        if len(tempvalue6) == 0:
                                            elem.send_keys(searchabledatabase.getrangeYear_1())

                                        text_area = driver.find_element_by_id("yr-go")
                                        text_area.click()

                    except Exception as e:
                        elem = elem
                    finally:
                        elem = elem
                    try:
                        if (find == 0):

                            elem = driver.find_element_by_name(classifyform.o_getTextBoxId_2())
                            value = elem.get_attribute("value")
                            elem = driver.find_element_by_name(classifyform.o_getTextBoxId_3())
                            value += elem.get_attribute("value")
                            elem = driver.find_element_by_name(classifyform.o_getTextBoxId_4())
                            value += elem.get_attribute("value")
                            elem = driver.find_element_by_name(classifyform.o_getTextBoxId_5())
                            value += elem.get_attribute("value")
                            print("I am in OLX")
                            a = len(value)
                            if (a == 0):
                                # elem = driver.find_element_by_id(searchableDatabase.o_getTextBoxId_1())
                                # elem.send_keys("old honda cars")
                                elem = driver.find_element_by_name(classifyform.o_getTextBoxId_2())
                                elem.send_keys(nlp.getrangeValue_1())
                                elem = driver.find_element_by_name(classifyform.o_getTextBoxId_3())
                                elem.send_keys(nlp.getrangeValue_2())
                                text_area = driver.find_element_by_class_name("VZrYe")
                                text_area.click()
                                time.sleep(4)

                                elem = driver.find_element_by_name(classifyform.o_getTextBoxId_4())
                                elem.send_keys(nlp.getrangeYear_1())
                                elem = driver.find_element_by_name(classifyform.o_getTextBoxId_5())
                                elem.send_keys(nlp.getrangeYear_2())

                                elem = driver.find_elements_by_class_name('VZrYe')[1]
                                # text_area = driver.find_element_by_class_name("VZrYe")
                                elem.click()

                                text_area = driver.find_element_by_class_name("rui-77aaa")
                                text_area.click()

                                elem = driver.find_elements_by_class_name("VZrYe")[1].click()
                                # text_area = driver.find_element_by_class_name("VZrYe")
                                # elem.click();
                    except Exception as e:
                        elem = elem;
                    finally:
                        elem = elem;
                    try:
                        if (find == 0):
                            try:
                                print("I am in other")
                                selectOption = Select(driver.find_element_by_id("make"))
                                option_selected = selectOption.select_by_value(searchableDatabase.get_company_name())
                            except Exception as e:
                                elem = elem;
                            finally:
                                try:
                                    selectOption = Select(driver.find_element_by_id("model"))
                                    option_selected = selectOption.select_by_value("X-PV")
                                except Exception as e:
                                    elem = elem;
                                finally:
                                    try:
                                        selectOption = Select(driver.find_element_by_id("year"))
                                        option_selected = selectOption.select_by_value(
                                            searchabledatabase.getrangeYear_1())
                                    except Exception as e:
                                        elem = elem;
                                    finally:
                                        try:
                                            selectOption = Select(driver.find_element_by_id("location"))
                                            option_selected = selectOption.select_by_value("lahore")
                                        except Exception as e:
                                            elem = elem;
                                        finally:
                                            try:
                                                selectOption = driver.find_element_by_name("submit_btn")
                                                selectOption.click()
                                            except Exception as e:
                                                elem = elem;

                    except Exception as e:
                        elem = elem;
                    finally:
                        elem = elem;
                        try:
                            if (find == 0):

                                word = "price"
                                a = 0
                                elem = driver.current_url;
                                print("I am in daraz")
                                if word in elem:
                                    a = 1
                                if (a == 0):
                                    try:
                                        selectOption = driver.find_element_by_class_name("c30Om7")
                                        tempvalue7 = selectOption.get_attribute("value")
                                        if len(tempvalue7) == 0:
                                            selectOption.send_keys(searchabledatabase.getrangeValue_2())

                                        ele = driver.find_element_by_xpath("//input[@placeholder='Max']")
                                        tempvalue8 = ele.get_attribute("value")
                                        if len(tempvalue8) == 0:
                                            ele.send_keys(searchabledatabase.getrangeValue_1())

                                        element = driver.find_element_by_class_name(
                                            "ant-btn.c3R9mX.ant-btn-primary.ant-btn-icon-only")
                                        element.click();


                                    except Exception as e:
                                        elem = e;
                                    finally:
                                        elem = elem;


                        except Exception as e:
                            elem = elem;
                        finally:
                            elem = elem;



