import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class BaseClass:
    load_dotenv()

    browsers = os.getenv("BROWSERS")
    browsers = browsers.split(", ")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    url = os.getenv("URL")

    @pytest.fixture(scope="class", autouse=True)
    def driver(self, request):
        browser = request.param
        BaseClass.current_browser = browser

        is_ci = os.getenv('CI') == 'true'
        if is_ci:
            if browser == "edge":
                options = EdgeOptions()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-extensions")
                options.add_argument("--disable-infobars")
                serv = EdgeService(EdgeChromiumDriverManager().install())
                driver = webdriver.Edge(service=serv, options=options)
            else:
                options = ChromeOptions()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-extensions")
                options.add_argument("--disable-infobars")
                serv = ChromeService(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=serv, options=options)
        else:
            if browser == "edge":
                options = EdgeOptions()
                options.add_argument("--disable-infobars")
                serv = (EdgeService(EdgeChromiumDriverManager().install()))
                driver = webdriver.Edge(service=serv, options=options)
            else:
                options = ChromeOptions()
                options.add_argument("--disable-infobars")
                serv = ChromeService(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=serv, options=options)

        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        driver.quit()
