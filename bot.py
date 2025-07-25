
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from data import email, password, des
import time


class StartBrowser:  # class 1
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://internshala.com/")
        self.increment = 0
        self.users = 2


class Autofill(StartBrowser):  # 2 (class 1 inheritance)
    def __init__(self) -> None:
        super().__init__()  # calling the parent class
        # self.Search = self.driver.find_element(By.NAME, "q")
        # self.Search.send_keys("Internshala" + Keys.ENTER)
        # WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "LC20lb"))
        # )
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "Internshala").click()
        # time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, "login-cta").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "modal_email").send_keys(email + Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.ID, "modal_password").send_keys(password + Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "main-heading"))
        )
        self.driver.get("https://internshala.com/internships/matching-preferences/")
        
        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.ID, "open_content_collapse"))
        )
        time.sleep(3)
        self.apply_internships()



    def apply_internships(self):  # 2.2 function
        
        try:
            preferences_checkbox = self.driver.find_element(By.ID, "matching_preference")
            if preferences_checkbox.is_selected():
                self.driver.execute_script("arguments[0].click();", preferences_checkbox)
                time.sleep(5)
        except NoSuchElementException:
            print("No preferences checkbox found.")

        try:
           
                dropdown = WebDriverWait(self.driver, 7).until(
                    EC.element_to_be_clickable((By.ID, "select_category"))
                )
                dropdown.click()
                time.sleep(2)
                
               
                dropdown_input = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input.chosen-search-input"))
                )
                dropdown_input.send_keys("web Development")
                time.sleep(2)
               
                web_dev_option = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'Web Development')]"))
                )
                self.driver.execute_script("arguments[0].click();", web_dev_option)
                time.sleep(2)
                
        except (TimeoutException, NoSuchElementException):
            print("Unable to find the dropdown or Web Development option.")



        # Proceed to apply for internships
        internships = self.driver.find_elements(By.CSS_SELECTOR, "#internship_list_container .individual_internship")
        while self.users>self.increment:
            internship = internships[self.increment]
            try:
                internship_name = internship.find_element(By.CLASS_NAME, "job-internship-name")
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "job-internship-name"))
                )
                self.driver.execute_script("arguments[0].click();", internship_name)
                print("over")
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "profile"))
                )
                time.sleep(3)
                self.driver.find_element(By.ID, "continue_button").click()
                #modal-content easy-apply
                #continue_button

                print("iner")
                
                # self.driver.find_element_by_css_selector('#check').click()

                div_element = self.driver.find_element(By.CSS_SELECTOR, ".heading_4_5.profile")
                inner_html = self.driver.execute_script("return arguments[0].innerHTML;", div_element)
                
                print(inner_html)
                # WebDriverWait(self.driver, 10).until(
                #     EC.element_to_be_clickable((By.CLASS_NAME, "ql-editor").send_keys(des)))
                try:
                    self.driver.find_element(By.CLASS_NAME, "ql-editor").send_keys(des)
                except Exception as e:



                
                # continue_button = self.driver.find_element(By.XPATH, "//span[text()='Continue applying']")
                # self.driver.execute_script("arguments[0].scrollIntoView();", continue_button)
                
                # WebDriverWait(self.driver, 10).until(
                #     EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue applying']"))
                # )
                # self.driver.execute_script("arguments[0].click();", continue_button)
                    print("started")
                    self.Relocation()
                    print("ended")
                    
                    not_interested_button = self.driver.find_element(By.ID, "dismiss_similar_job_modal")
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "dismiss_similar_job_modal"))
                    )
                    self.driver.execute_script("arguments[0].click();", not_interested_button)
                    
                    WebDriverWait(self.driver, 10).until(
                        EC.url_contains("internships/matching-preferences")
                    )

                    time.sleep(2)
                    self.driver.find_element(By.ID, " back-cta").click()
                finally:
                    self.Relocation()
                    print("ended")
                    
                    not_interested_button = self.driver.find_element(By.ID, "dismiss_similar_job_modal")
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.ID, "dismiss_similar_job_modal"))
                    )
                    self.driver.execute_script("arguments[0].click();", not_interested_button)
                    
                    WebDriverWait(self.driver, 10).until(
                        EC.url_contains("internships/matching-preferences")
                    )

                    time.sleep(2)
                    self.driver.find_element(By.ID, "back-cta").click()

            except Exception as e:
                print(f"Error processing internship: {e}")
            # finally:
            #         self.increment += 1 


    def Relocation(self):
        try:
            Relocation = self.driver.find_element(By.CSS_SELECTOR, "label[for='check']")
            if Relocation.is_displayed():
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='check']"))
                ).click()
                time.sleep(2)
                self.Assesment()
            else:
                self.Assesment()
        except NoSuchElementException:
            self.Assesment()

    def Assesment(self):
        try:
            self.driver.execute_script('window.scrollBy(0, 1000)')
            Assessment = self.driver.find_element(By.CLASS_NAME, "additional_question")
            Assessment_Questions = self.driver.find_elements(By.CLASS_NAME, "additional_question")
            if Assessment.is_displayed():
                for i in Assessment_Questions:
                    time.sleep(5)
                    textarea = i.find_element(By.CSS_SELECTOR, "textarea")
                    attr = textarea.get_attribute("id")
                    WebDriverWait(self.driver, 20).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, f"textarea[id='{attr}']"))
                    ).send_keys("This form is submitted by Bot,\nSorry!!")
                self.EndForm()
            else:
                self.EndForm()
        except Exception as ec:
            print(ec)
            self.EndForm()

    def EndForm(self):
        self.driver.find_element(By.ID, "submit").click()
        time.sleep(5)
        self.increment+=1
        if self.increment == self.users:
           self.driver.close()
if __name__ == "__main__":  #1
    start = Autofill() 
    input("Press any key")
