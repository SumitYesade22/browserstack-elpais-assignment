from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraper import get_first_five_opinion_links, extract_article_data
from translator import translate_text


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def main():
    driver = get_driver()
    translated_titles = []

    try:
        links = get_first_five_opinion_links(driver)

        for i, link in enumerate(links, start=1):
            print("\n============================")
            print(f"Article {i}")
            print("============================")

            data = extract_article_data(driver, link)

            print("\nSpanish Title:")
            print(data["title"])

            print("\nContent Preview:")
            print(data["content"][:300])

            print("\nImage URL:")
            print(data["image_url"])

            # 🔹 Translation happens here
            translated = translate_text(data["title"])
            translated_titles.append(translated)

            print("\nTranslated Title (English):")
            print(translated)

        print("\n============================")
        print("All Translated Titles")
        print("============================")

        for t in translated_titles:
            print("-", t)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
