from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraper import get_first_five_opinion_links
from scraper import get_first_five_opinion_links, extract_article_data


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def main():
    driver = get_driver()

    try:
        links = get_first_five_opinion_links(driver)

        print("First 5 Opinion Articles:")
        for i, link in enumerate(links, start=1):
            print(f"{i}. {link}")

    finally:
        driver.quit()

def main():
    driver = get_driver()

    try:
        links = get_first_five_opinion_links(driver)

        for i, link in enumerate(links, start=1):
            print(f"\nArticle {i}")
            data = extract_article_data(driver, link)

            print("Title:", data["title"])
            print("Content preview:", data["content"][:300])
            print("Image URL:", data["image_url"])

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
