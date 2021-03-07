from behave import step
from selenium import webdriver
from time import sleep


# @step('Navigate to Google')
# def test(context):
#     driver = webdriver.Chrome("C:/Python39/Scripts/chromedriver.exe")   # path for windows #
#     driver.get("https://www.google.com/")
#     print("Navigate OK")
#
#
# @step('Open eBay.com')
# def some_test_imp(context):
#     context.browser = webdriver.Chrome()
#     context.browser.get("https://www.ebay.com/")
#     print("Open eBay.com OK")
#
#
# @step('Search for "dress"')
# def search_smth(context):
#     search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
#     search_inpt.send_keys("dress")
#     print("Search OK")
#
#
# @step('Click the Search button')
# def click_the_search_btn(context):
#     search_btn = context.browser.find_element_by_xpath("//input[@id='gh-btn']")
#     search_btn.click()
#     sleep(2)
#     print("Click the Search button OK")


# @step('All items are somewhat dress related')
# def verify_search_result(context):
#     item = context.browser.find_element_by_xpath("//h3[text()='Women Ladies Long Maxi Dress Boho Holiday Beach Party Cocktail Summer Sundress']")


# @step('Go to shopping cart')
# def verify_shopping_cart(context):
#     context.browser = webdriver.Chrome()
#     context.browser.get("https://www.ebay.com/")
#     cart = context.browser.find_element_by_xpath("//a[@title='Your shopping cart']")
#     cart.click()
#     cart_title = context.browser.find_element_by_xpath("//h1[text()='Shopping cart']").text
#     assert 'Shopping cart' == cart_title
#     sleep(2)
#     print("Cart OK")
#
#
# @step('Go to Sell')
# def verify_sell(context):
#     context.browser.get("https://www.ebay.com/")
#     sell = context.browser.find_element_by_xpath("//li[@id='gh-p-2']")
#     sell.click()
#     sell_title = context.browser.find_element_by_xpath("//h1[@class='home-pagetitle']").text
#     assert 'Selling' == sell_title
#     sleep(2)
#     print("Sell OK")
#
#
# @step('Go to Help & Contact')
# def verify_help(context):
#     context.browser.get("https://www.ebay.com/")
#     help = context.browser.find_element_by_xpath("//a[text()=' Help & Contact']")
#     help.click()
#     help_title = context.browser.find_element_by_xpath("//button[text()='Help']").text
#     assert "Help" == help_title
#     sleep(2)
#     print("Help OK")
#
#
# @step('Go to Brand Outlet')
# def verify_brand_outlet(context):
#     context.browser.get("https://www.ebay.com/")
#     context.browser.maximize_window()
#     brand = context.browser.find_element_by_xpath("//a[text()=' Brand Outlet']")
#     brand.click()
#     brand_title = context.browser.find_element_by_xpath("//span[text()='The Brand Outlet']").text
#     assert "The Brand Outlet" == brand_title
#     sleep(2)
#     print("Brand OK")
#
#
# @step('Go to Daily Deals')
# def verify_daily_deals(context):
#     context.browser.get("https://www.ebay.com/")
#     deals = context.browser.find_element_by_xpath("//a[text()=' Daily Deals']")
#     deals.click()
#     deals_title = context.browser.find_element_by_xpath("//a[text()='Deals']").text
#     assert "Deals" == deals_title
#     sleep(2)
#     print("Deals OK")


# @step('Open eBay.com')
# def some_test_imp(context):
#     context.browser = webdriver.Chrome()
#     context.browser.get("https://www.ebay.com/")
#     print("Open eBay.com OK")
#
#
# @step('Click Sign In')
# def sign_in(context):
#     sing_in = context.browser.find_element_by_xpath("//a[@_sp='m570.l1524' and  text()='Sign in']")
#     sing_in.click()
#     sleep(3)
#     print("Click Sign In")
#
#
# @step('Input email')
# def email(context):
#     email_field = context.browser.find_element_by_xpath("//input[@id='userid']")
#     email_field.send_keys("akradabaska@gmail.com")
#     sleep(2)
#     print("Input email OK")
#
#
# @step('Click Continue')
# def cont(context):
#     cont = context.browser.find_element_by_xpath("//button[@id='signin-continue-btn']")
#     cont.click()
#     sleep(2)
#     print("Click Continue OK")
#
#
# @step('Input wrong password')
# def password(context):
#     pass_field = context.browser.find_element_by_xpath("//input[@id='pass']")
#     pass_field.send_keys("123123123")
#     sleep(2)
#     print("Input wrong password OK")
#
#
# @step('Click Sign In button')
# def cont_btn_click(context):
#     cont_btn = context.browser.find_element_by_xpath("//button[@id='sgnBt']")
#     cont_btn.click()
#     sleep(2)
#     print("Click Sign In button OK")
#
#
# @step('Verify fail')
# def verify_fail(context):
#     fail = context.browser.find_element_by_xpath("//p[@id='signin-error-msg']").text
#     assert "Oops, that's not a match." == fail
#     sleep(2)
#     print("Verify fail OK")