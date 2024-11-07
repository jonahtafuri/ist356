# ## Challenge 5-1-2:

# Create an outline!

# Scrape the Sections H2 and H3 from this page:  https://ist256.com/fall2023/syllabus/

# Print the titles, and detect the tag name so that you indent the H3 tags under the H2 tags.

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ist256.com/fall2023/syllabus/")

    # outer element that contains the list of 250 top movies
    headings = page.query_selector_all("h2, h3")

    for heading in headings:
        tag = heading.evaluate("(el) => el.tagName")
        # print(tag)
        if tag == "H2":
            text = heading.inner_text()
            print(text)
        elif tag == "H3":
            text = heading.inner_text()
            print(f"    {text}")


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)