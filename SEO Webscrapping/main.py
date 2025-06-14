from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import pandas as pd
import time


def create_driver():
    options = uc.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = uc.Chrome(options=options)
    return driver


def get_html(driver, query):
    driver.get(f"https://www.google.com/search?q={query}&num=50")
    time.sleep(5)
    html = driver.page_source
    driver.quit()
    return html


def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='tF2Cxc')
    data = []

    for index, result in enumerate(results):
        title_elem = result.find('span', class_="VuuXrf")
        link_elem = result.find('a')

        if title_elem and link_elem:
            company = title_elem.text.strip()
            website = link_elem['href'].strip()
            data.append({"Rank": index + 1, "Company": company, "Website": website})

    return data


def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    df.to_csv(filename, index=False)


def main():
    query = "web development companies"
    driver = create_driver()
    html = get_html(driver, query)
    data = parse_results(html)
    save_to_csv(data, "companies.csv")


if __name__ == "__main__":
    main()