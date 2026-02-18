from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraper import get_first_five_opinion_links, extract_article_data
from translator import translate_text
from analyzer import find_repeated_words


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
            
            print(f"Article {i}")
            print("______________________")

            data = extract_article_data(driver, link)

            print("\nSpanish Title:")
            print(data["title"])

            print("\nContent Preview:")
            print(data["content"][:300])

            print("\nImage URL:")
            print(data["image_url"])

            # Translation
            translated = translate_text(data["title"])
            translated_titles.append(translated)

            print("\nTranslated Title (English):")
            print(translated)

       
      
        print("All Translated Titles")
        print("_________________________")

        for t in translated_titles:
            print("-", t)

     
        repeated_words = find_repeated_words(translated_titles)

       
        print("Repeated Words (Count >= 3)")
       

        if repeated_words:
            for word, count in repeated_words.items():
                print(f"{word} -> {count}")
        else:
            print("No words repeated more than twice.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
