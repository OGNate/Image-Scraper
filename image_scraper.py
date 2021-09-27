from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

DRIVER_PATH = "C:\\Users\\motonite29.DESKTOP-SNHF63L\\Desktop\Scraping\\chromedriver_win32\\chromedriver"

def scraper_main():
    driver = webdriver.Chrome(executable_path = DRIVER_PATH)
    driver.get("https://www.google.com/")

    google_search(driver)   # Google Searches for an item
    

    time.sleep(2)

    driver.quit()   # Exits the driver


def google_search(driver):
    search_bar = driver.find_element_by_name("q")   # Finds the search Bar in google
    search_bar.send_keys("Hello")
    search_bar.send_keys(Keys.ENTER)



if __name__ == "__main__":
    scraper_main()