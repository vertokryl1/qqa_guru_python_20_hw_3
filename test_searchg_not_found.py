from selene import browser, have

def test_search(open_browser_with_size):
    browser.element('[name="q"]').type('t5ru5656i67o67o7op').press_enter()
    browser.element('html').should(have.text('ничего не найдено.'))
