from playwright.sync_api import Playwright, sync_playwright, expect
import pandas as pd

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/syllabus/")

    # Let's scrape the page!
    # use pandas read_html to parse the HTML

    # get a list of all tables on the page
    start_element = page.query_selector("h4#criteria-for-project-grade")
    next_element = start_element.query_selector("~ *")
    bullet_elements = next_element.query_selector_all("li")
    
    criteria = []
    for element in bullet_elements:
        criteria.append(element.inner_text())


    context.close()
    browser.close()
    
    return criteria

with sync_playwright() as playwright:
    criteria = run(playwright)
    print(criteria)