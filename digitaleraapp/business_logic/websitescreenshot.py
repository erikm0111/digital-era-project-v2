import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebsiteScreenshot:

    def capture(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})
        chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.cookies" : 2 })
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("http://festino.hr/")
        time.sleep(5)
        self.save_screenshot(driver)

    def save_screenshot(self, driver: webdriver.Chrome, path: str = 'screenshot.png') -> None:
        # Ref: https://stackoverflow.com/a/52572919/
        original_size = driver.get_window_size()
        required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(required_width, required_height)
        driver.find_element_by_tag_name('body').screenshot(path)
        driver.set_window_size(original_size['width'], original_size['height'])

if __name__ == '__main__':
    scrn = WebsiteScreenshot()
    scrn.capture()