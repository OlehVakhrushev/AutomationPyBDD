#Feature: Hello world
#
# Scenario: Test
#   Given Navigate to Google

Feature: Regression for Ebay
  @bvt
  Scenario: 1: Verify that search display right items
    Given Open eBay.com
    And Search for "dress"
    And Click the Search button
    And Close browser

#    Then All items are somewhat dress related
#    And Navigate to shopping cart

  @bvt
  Scenario: 2: Verify Top Bar functions (Sell)
    Given Open eBay.com
    And Verify that "Sell" is visible on the page
    And Click "Sell" header element
    And User is redirected to "Sell" page
    Then Close browser

  @lol
    Scenario: 3: Verify Top Bar functions (Help & Contact)
    Given Open eBay.com
    And Verify that "Help & Contact" is visible on the page
    And Click "Help & Contact" header element
    And User is redirected to "Help & Contact" page
    Then Close browser

  @bvt
    Scenario: 4: Verify Top Bar functions (Brand Outlet)
    Given Open eBay.com
    And Verify that "Brand Outlet" is visible on the page
    And Click "Brand Outlet" header element
    And User is navigated to "Brand Outlet"
    And Close browser

  @bvt
    Scenario: 5: Verify Top Bar functions (Daily Deals)
    Given Open eBay.com
    And Verify that "Daily Deals" is visible on the page
    And Click "Daily Deals" header element
    And User is redirected to "Daily Deals"
    And Close browser

  @bvt
  Scenario: 3: Find product and show the price
    Given Open eBay.com
    Then Search toy product
    And Click Search
    Then Show price of first product

  @bvt
  Scenario: 4: Verify Sign In with wrong password and email
    Given Open eBay.com
    And Click Sign In
    And Input email
    And Click Continue
    And Input wrong password
    And Click Sign In button
    Then Verify fail

  @bvt
  Scenario: 5: Use search with srt and num
    Given Open eBay.com
    And Search for "dress123"
    And Click Search
    Then Show results

  @bvt
  Scenario: 6: Use search with numbers only
    Given Open eBay.com
    And Search for 123
    And Click Search
    Then Show results

  @bvt
  Scenario: 7: Use search with num, str, spec characters
    Given Open eBay.com
    And Search for "dress234#$%"
    And Click Search
    Then Show results

  @empty
  Scenario: 8: Use search with space " "
    Given Open eBay.com
    And Search for " "
    And Click Search
    Then Show results errors

  @bvt
  Scenario: 9: Search for Iphone 11
    Given Open eBay.com
    And Search Iphone 11 product
    And Click Search
    And Show all results with Free shipping, Free returns
#    And Show all result with Free 3 day shipping  //$x("//li[@class = 's-item    '][.//span[text()='Free 3 day shipping']]")
#    And Show all results with Free 4 day shipping
#    And Show all results 60 Day Warranty and Charger Included
#    And Show all results with Free returns, Free 3 day shipping, 60 Day Warranty and Charger Included


