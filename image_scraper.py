from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""
    To-Do:
        1) Continue reading in images
"""

DRIVER_PATH = "C:\\Users\\motonite29.DESKTOP-SNHF63L\\Desktop\Scraping\\chromedriver_win32\\chromedriver"

def scraper_main():
    driver = webdriver.Chrome(executable_path = DRIVER_PATH)

    google_search("trash cans", 10, driver, 1)   # Google Searches for an item


    time.sleep(2)

    driver.quit()   # Exits the driver


def google_search(search_word: str, number_imgs: int, driver: webdriver, sleep_between_intervals: int = 1):
    
    def scroll_to_end(driver: webdriver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_intervals)

    driver.get("https://www.google.com/")
    search = driver.find_element_by_name("q")
    search.send_keys(search_word)
    search.send_keys(Keys.ENTER)




if __name__ == "__main__":
    scraper_main()