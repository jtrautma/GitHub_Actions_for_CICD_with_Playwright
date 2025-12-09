from playwright.sync_api import Page, expect

def test_successful_playwright_docs_page(page: Page) :
    page.goto('https://playwright.dev/python/')
    headline = page.locator('h1.hero__title')
    expect(headline).to_have_text('Playwright enables reliable end-to-end testing for modern web apps.')

# '''
def test_failed_playwright_docs_page(page: Page) :
    page.goto('https://playwright.dev/python/')
    headline = page.locator('h1.hero__title')
    expect(headline).not_to_contain_text('reliable')
# '''
