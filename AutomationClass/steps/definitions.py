from behave import step
from selenium import webdriver
from time import sleep


# @step('Navigate to Google')
# def test(context):
#     driver = webdriver.Chrome("C:/Python39/Scripts/chromedriver.exe")
#     driver.get("https://www.google.com/")


@step('Open eBay.com')
def some_test_imp(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.ebay.com/")


@step('Search for "dress"')
def search_smth(context):
    search_inpt = context.browser.find_element_by_xpath("//input[@id='gh-ac']")
    search_inpt.send_keys("dress")


@step('Click the Search button')
def click_the_search_btn(context):
    search_btn = context.browser.find_element_by_xpath("//input[@id='gh-btn']")
    search_btn.click()
    sleep(5)


@step('All items are somewhat dress related')
def verify_search_result(context):
    item = context.browser.find_element_by_xpath("//h3[text()='Women Ladies Long Maxi Dress Boho Holiday Beach Party Cocktail Summer Sundress']")
