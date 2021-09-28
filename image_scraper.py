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


def google_search(search_word: str, max_number_imgs: int, driver: webdriver, sleep_between_intervals: int = 1):
    
    def scroll_to_end(driver: webdriver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_intervals)

    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    
    driver.get(search_url.format(q = search_word))  # Loads the image page of the search word


    image_urls = set()
    image_count, results_start = 0, 0

    while image_count < max_number_imgs:
        scroll_to_end(driver)

        thumbnail_results = driver.find_element_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)

        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

        break
    
    




if __name__ == "__main__":
    scraper_main()