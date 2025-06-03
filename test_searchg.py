from selene import browser, have

def test_search(open_browser_with_size):
    browser.element('[name="q"]').type('qa.guru').press_enter()

