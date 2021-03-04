from behave import step
from selenium import webdriver


@step('Navigate to Google')
def test(context):
    driver = webdriver.Chrome("C:/Python39/Scripts/chromedriver.exe")
    driver.get("https://www.google.com/")
