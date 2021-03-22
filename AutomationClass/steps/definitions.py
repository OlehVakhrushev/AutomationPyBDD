from behave import step
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


# @step('Navigate to Google')
# def test(context):
#     driver = webdriver.Chrome("C:/Python39/Scripts/chromedriver.exe")   # path for windows #
#     driver.get("https://www.google.com/")
#     print("Navigate OK")



@step('Open eBay.com')
def some_test_imp(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
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


# @step('Search for "{search_product}"')
# def show_iphone_deals(context, search_product):
#     search = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
#     search.send_keys(f"{search_product}", Keys.ENTER)
#     sleep(5)


@step('In search bar type "{search_product}" from the keyboard')
def pr_enter(context, search_product):
    press_enter = context.browser.find_element_by_xpath(
        "//div[@id = 'gh-ac-box2']/input[@class = 'gh-tb ui-autocomplete-input']")

    if not press_enter:
        raise ValueError("Search bar is not located")
    else:
        press_enter.send_keys(f"{search_product}", Keys.ENTER)
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


# @step('Verify that results are related to "{search_product}" on 20 pages')
# def verify_relevant_results(context, search_product):
#     result_items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')]//h3")
#     fails = []
#     for each_item in result_items:
#         if search_product.lower() not in each_item.lower():
#             fails.append(each_item.text)
#     if fails:
#         print(fails)
#         raise ValueError(f"Some items are not {search_product} related")
#
#
# def verify_relevant_results_on_pages(context, search_product, pages):
#     max_page = int(pages)
#     current_page = 1
#     while current_page < max_page:
#         verify_relevant_results(context, search_product)
#         current_page = click_next_page(context.browser)
#
#
# def click_next_page(browser):
#     next_page = browser.find_element_by_xpath("//div[@class='s-pagination']//a[@type='next']")
#     next_page.click()
#     current_page_item = browser.find_element_by_xpath("//div[@class='s-pagination']//a[@aria-current='page']")
#     page_number = int(current_page_item.text)
#     return page_number


# @step('Verify that results are related to "{search_product}" on 20 pages')
# def verify_relevant_results(context, search_product):
#     pages = context.browser.find_elements_by_xpath("//a[@class='pagination__item']")
#     number = len(pages)
#     items = context.browser.find_elements_by_xpath("//li[contains(@class,'s-item')]//h3")
#     for page in range(1, 40):
#         sleep(4)
#         page.click()
#         context.browser.find_elements_by_xpath(f"//a[@class='pagination__item' anf text()='{page}']").click()
#         sleep(4)
#
#         fails = []
#         for each_item in items:
#             if search_product.lower() not in each_item.text:
#                 fails.append(each_item.text)
#
#         if fails:
#             number=len(fails)
#             print(number)
#             print(fails)
#             raise ValueError(f'Some products are not {search_product} related')


@step('Verify that search results are relevant to "{name_of_search_keyword}" on the all pages of the search')
def verification_of_search_results(context, name_of_search_keyword):
    ver_of_search = context.browser.find_elements_by_xpath("//li[starts-wth[@class = 's-item']//h3]")
    next_page_result = context.browser.find_elements_by_xpath("//a[@class = 'pagination__next']")
    fails = []
    while ver_of_search:
        ver_item = ver_of_search[0]
        if name_of_search_keyword.lower() not in ver_item.text.lower():
            fails.append(ver_item.text)
            ver_of_search.delete(0)
        if fails:
            raise ValueError(f'Some of items are not "{name_of_search_keyword}" related')

    while next_page_result: # Till the end
        next_page_button_disable = context.browser.find_elements_by_xpath("//a[@class = 'pagination__next' and @aria-disabled = 'true']")
        if next_page_button_disable:
            break
        for page in next_page_result:
            page.click()
            sleep(1)
            next_page_result = context.browser.find_elements_by_xpath("//a[@class = 'pagination__next']")


@step('Filter "{search_product}" by "{filter_header}" in category "{filter_option}"')
def filter_checker(context, search_product, filter_header, filter_option):
    desired_ckbx = context.browser.find_elements_by_xpath(f"//li[@class='x-refine__main__list '][.//h3[text()='{filter_header}']]"
                                                          f"//div[@class='x-refine__select__svg'][.//span[text()='{filter_option}']]//input")

    if not desired_ckbx:
        raise ValueError(f'No {search_product} filtered by {filter_header} in {filter_option}')
    desired_ckbx[0].click()
    sleep(5)
    print("Now we can check it again")
    if desired_ckbx:
        print(f"Now {search_product} is {filter_header} by {filter_option}")
    sleep(2)
    context.browser.close()