from behave import step
from selenium import webdriver
from time import sleep



# @step('Navigate to Google')
# def test(context):
#     driver = webdriver.Chrome("C:/Python39/Scripts/chromedriver.exe")   # path for windows #
#     driver.get("https://www.google.com/")
#     print("Navigate OK")

@step('Open eBay.com')
def some_test_imp(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.ebay.com/")
    print("Open eBay.com OK")


@step('Search for "dress"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dress")
    print("Search OK")


@step('Click the Search button')
def click_the_search_btn(context):
    search_btn = context.browser.find_element_by_xpath("//input[@id='gh-btn']")
    search_btn.click()
    sleep(2)
    print("Click the Search button OK")


@step('Close browser')
def close_browser(context):
    context.browser.close()


@step('Navigate to shopping cart')
def verify_shopping_cart(context):
    cart = context.browser.find_element_by_xpath("//a[@title='Your shopping cart']")
    cart.click()
    cart_title = context.browser.find_element_by_xpath("//h1[text()='Shopping cart']").text
    assert 'Shopping cart' == cart_title
    sleep(2)
    print("Cart OK")


@step('Verify that "{name_of_header_element}" is visible on the page')
def header_element_sell(context, name_of_header_element):
    context.browser.maximize_window()
    header_sell = context.browser.find_element_by_xpath(f"//a[@class='gh-p' and contains(text(), '{name_of_header_element}')]")


@step('Click "{action_of_header_element}" header element')
def click_header_sell(context, action_of_header_element):
    header_sell_action = context.browser.find_element_by_xpath(f"//a[@class='gh-p' and contains(text(), '{action_of_header_element}')]")
    sleep(2)
    header_sell_action.click()


@step('User is redirected to "Sell" page')
def open_sell_page(context):
    sell_open = context.browser.find_element_by_xpath("//h1[@class = 'home-pagetitle']").text
    print(f"{sell_open}")
    sleep(2)


@step('User is redirected to "Help & Contact" page')
def open_help_page(context):
    help_open = context.browser.find_element_by_xpath("//td[@id = 'gh-title']").text
    print(f"{help_open}")
    sleep(2)


@step('User is navigated to "Brand Outlet"')
def open_brand_page(context):
    brand_title = context.browser.find_element_by_xpath("//span[@class='b-pageheader__text']").text
    print(f"{brand_title}")
    sleep(2)


@step('User is redirected to "Daily Deals"')
def open_deals_page(context):
    deals_title = context.browser.find_element_by_xpath("//a[text() = 'Deals']").text
    print(f"{deals_title}")
    sleep(2)


@step('Click Sign In')
def sign_in(context):
    sing_in = context.browser.find_element_by_xpath("//a[@_sp='m570.l1524' and  text()='Sign in']")
    sing_in.click()
    sleep(3)
    print("Click Sign In")


@step('Input email')
def email(context):
    email_field = context.browser.find_element_by_xpath("//input[@id='userid']")
    email_field.send_keys("akradabaska@gmail.com")
    sleep(2)
    print("Input email OK")


@step('Click Continue')
def cont(context):
    cont = context.browser.find_element_by_xpath("//button[@id='signin-continue-btn']")
    cont.click()
    sleep(2)
    print("Click Continue OK")


@step('Input wrong password')
def password(context):
    pass_field = context.browser.find_element_by_xpath("//input[@id='pass']")
    pass_field.send_keys("123123123")
    sleep(2)
    print("Input wrong password OK")


@step('Click Sign In button')
def cont_btn_click(context):
    cont_btn = context.browser.find_element_by_xpath("//button[@id='sgnBt']")
    cont_btn.click()
    sleep(2)
    print("Click Sign In button OK")


@step('Verify fail')
def verify_fail(context):
    fail = context.browser.find_element_by_xpath("//p[@id='signin-error-msg']").text
    assert "Oops, that's not a match." == fail
    sleep(2)
    print("Verify fail OK")


@step('Search {search_product} product')
def search_toy(context, search_product):
    search = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search.send_keys("{}".format(search_product))
    sleep(2)
    print("Search product OK")


@step('Click Search')
def click_search(context):
    search_btn = context.browser.find_element_by_xpath("//input[@id='gh-btn']")
    search_btn.click()
    sleep(2)
    print("Click Search OK")


@step('Show price of first product')
def show_price(context):
    price = context.browser.find_element_by_xpath("//span[@class='s-item__price']").text
    sleep(3)
    print(f"Show price of first product OK and {price}")



@step('Search for "dress123"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dress123")
    sleep(2)
    print("Search OK")


@step('Show results')
def show_res(context):
    res = context.browser.find_element_by_xpath("//h1[@class='srp-controls__count-heading']").text
    print(f"{res}  <=== Here is your results")
    sleep(2)
    print("Show results OK")


@step('Search for "dress123%^&&"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dress123%^&&")
    sleep(2)
    print("Search OK")


@step('Search for 123')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("123")
    sleep(2)
    print("Search OK")


@step('Search for " "')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys(" ")
    sleep(2)
    print("Search OK")


@step('Show results errors')
def show_res(context):
    res_error = context.browser.find_element_by_xpath("//div[@class='s-message__content']").text
    print(f"{res_error}  <=== Here is your error result with space search")
    sleep(2)
    print("Show results OK")


@step('Search for Iphone 11')
def show_iphone_deals(context, search_product):
    search = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search.send_keys("{}".format(search_product))
    sleep(5)


@step('Show all results with Free shipping, Free returns')
def show_res(context):
    results = context.browser.find_elements_by_xpath("//li[@class = 's-item    '][.//span[text()='Free shipping']][.//span[text() = 'Free returns']][.//span[text() = 'Buy It Now']]//h3")
    count = len(results) + 1
    print("*****")
    print(f"{count}")
    print("*****")


@step('Show all results with Free 3 day shipping')
def show_res(context):
    results = context.browser.find_elements_by_xpath("//li[@class='s-item     '][.//div[@class='s-item__info clearfix'][.//span[@class='POSITIVE BOLD' and text()='Free 3 day shipping']]]")
    count = len(results) + 1
    print("*****")
    print(f"{count}")
    print("*****")


@step('Check if results is 10')
def show_res(context):
    results = context.browser.find_elements_by_xpath("//li[@class='s-item     '][.//div[@class='s-item__info clearfix'][.//span[@class='POSITIVE BOLD' and text()='Free 3 day shipping']]]")
    count = len(results)
    print("*****")
    print(f"{count}")
    print("*****")
    if count != 10:
        raise ValueError(f'Oleh, we have a problem: \n\n We missing good deal for Iphone 11')
    else:
        print("We good")
