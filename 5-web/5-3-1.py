import streamlit as st
from playwright.sync_api import Playwright, sync_playwright
from time import sleep


def run(playwright: Playwright, url) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    sleep(2)

    continue