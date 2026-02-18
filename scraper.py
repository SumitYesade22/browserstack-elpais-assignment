from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import requests


def handle_cookie_popup(driver):
    wait = WebDriverWait(driver, 5)
    try:
        accept_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Aceptar') or contains(., 'Accept')]")
            )
        )
        accept_button.click()
    except:
        pass


def get_first_five_opinion_links(driver):
    driver.get("https://elpais.com/opinion/")
    handle_cookie_popup(driver)

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article h2 a"))
    )

    articles = driver.find_elements(By.CSS_SELECTOR, "article h2 a")

    links = []
    for article in articles[:5]:
        href = article.get_attribute("href")
        if href:
            links.append(href)

    return links


def extract_article_data(driver, url, image_folder="images"):
    driver.get(url)

    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

   
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "No Title Found"

  
    content = ""

   
    container = soup.select_one("div.a_e_txt_df")
    if container:
        content = container.get_text(separator="\n", strip=True)

  
    if not content:
        container = soup.select_one("div[data-dtm-region='articulo_cuerpo']")
        if container:
            content = container.get_text(separator="\n", strip=True)

   
    if not content:
        container = soup.select_one("article")
        if container:
            content = container.get_text(separator="\n", strip=True)

    
    if not content:
        content = soup.get_text(separator="\n", strip=True)

    
    image_url = None
    image_tag = soup.select_one("figure img")

    if image_tag and image_tag.get("src"):
        image_url = image_tag["src"]

    # the image is downloaded here sir
    if image_url:
        os.makedirs(image_folder, exist_ok=True)

        image_name = url.split("/")[-1] + ".jpg"
        image_path = os.path.join(image_folder, image_name)

        try:
            response = requests.get(image_url, timeout=10)
            if response.status_code == 200:
                with open(image_path, "wb") as f:
                    f.write(response.content)
        except:
            pass

    return {
        "title": title,
        "content": content,
        "image_url": image_url
    }
