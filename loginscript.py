from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants

driver = webdriver.Chrome(executable_path=constants.PATH)

def open_smhw():
    driver.get(constants.SMHW_URL)
    accept_terms = get_element_wait('//*[@id="onetrust-accept-btn-handler"]')
    accept_terms.click()
    #outlook_login_btn = get_element_wait('/html/body/div[3]/div[2]/div/div/div[1]/form/div[5]/div/button[1]/span')
    #outlook_login_btn.click()

def main():
    open_smhw()

def get_element_wait(xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element
    finally:
        driver.close()

if __name__ == "__main__":
    main()