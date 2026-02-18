import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv

from scraper import get_first_five_opinion_links, extract_article_data
from translator import translate_text

load_dotenv()

USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub"


def run_full_test(capability_config):
    options = Options()

    options.set_capability("browserName", capability_config["browserName"])
    if "browserVersion" in capability_config:
        options.set_capability("browserVersion", capability_config["browserVersion"])

    options.set_capability("bstack:options", capability_config["bstack:options"])

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    try:
        print(f"Starting: {capability_config['bstack:options']['sessionName']}")

        links = get_first_five_opinion_links(driver)

        translated_titles = []

        for link in links:
            data = extract_article_data(driver, link)

            translated = translate_text(data["title"])
            translated_titles.append(translated)

        print(f"Completed: {capability_config['bstack:options']['sessionName']}")

    except Exception as e:
        print(f"Error in {capability_config['bstack:options']['sessionName']}:", e)

    finally:
        driver.quit()


def main():
    capability_list = [
        {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "Windows",
                "osVersion": "11",
                "buildName": "ElPais Parallel Build",
                "sessionName": "Windows 11 - Chrome"
            }
        },
        {
            "browserName": "Edge",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "Windows",
                "osVersion": "11",
                "buildName": "ElPais Parallel Build",
                "sessionName": "Windows 11 - Edge"
            }
        },
        {
            "browserName": "Safari",
            "browserVersion": "latest",
            "bstack:options": {
                "os": "OS X",
                "osVersion": "Ventura",
                "buildName": "ElPais Parallel Build",
                "sessionName": "macOS Ventura - Safari"
            }
        },
        {
            "browserName": "Chrome",
            "bstack:options": {
                "deviceName": "Samsung Galaxy S22",
                "realMobile": "true",
                "osVersion": "12.0",
                "buildName": "ElPais Parallel Build",
                "sessionName": "Samsung Galaxy S22 - Chrome"
            }
        },
        {
            "browserName": "Safari",
            "bstack:options": {
                "deviceName": "iPhone 14",
                "realMobile": "true",
                "osVersion": "16",
                "buildName": "ElPais Parallel Build",
                "sessionName": "iPhone 14 - Safari"
            }
        }
    ]

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(run_full_test, capability_list)


if __name__ == "__main__":
    main()
