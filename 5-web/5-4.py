import re
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
import pandas as pd


def run(playwright: Playwright, search:str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url = f"https://syracuse.craigslist.org/search/sss?query={search}#search=1~list~0~0"
    page.goto(url)
    sleep(2)
    listings_selector = page.query_selector("div.results")
    items = listings_selector.query_selector_all("div.result-node")
    scraped = []
    for item in items:
        title = item.query_selector("span.label").inner_text()
        price = item.query_selector("span.priceinfo")
        if price:
            price = price.inner_text()
        else:
            price = "N/A"
        scraped_item = {
            "title": title,
            "price": price,
            "location": "Syracuse, NY",
        }
        scraped.append(scraped_item)
    # ---------------------
    context.close()
    browser.close()

    df = pd.DataFrame(scraped)
    df.to_csv(f"./5-web/cache/craigslist_data_{search}.csv", index=False)




with sync_playwright() as playwright:
    run(playwright, "silent hill")