from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://finance.yahoo.com/quote/AAPL/")
    
    price_selector = page.query_selector("fin-streamer.livePrice")
    price = price_selector.inner_text()
    print("AAPL", price)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

run()