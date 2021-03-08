#Feature: Hello world
#
# Scenario: Test
#   Given Navigate to Google

Feature: Regression for Ebay

  Scenario: Verify that search display right items
    Given Open eBay.com
    And Search for "dress"
    And Click the Search button
#    Then All items are somewhat dress related


  Scenario: Verify Top Bar functions
    Given Go to shopping cart
    And Go to Sell
    And Go to Help & Contact
    And Go to Brand Outlet
    Then Go to Daily Deals

  Scenario: Find product and show the price
    Given Open eBay.com
    Then Search toy product
    And Click Search
    Then Show price of first product

  Scenario: Verify Sign In with wrong password and email
    Given Open eBay.com
    And Click Sign In
    And Input email
    And Click Continue
    And Input wrong password
    And Click Sign In button
    Then Verify fail

  Scenario: Use search with srt and num
    Given Open eBay.com
    And Search for "dress123"
    And Click Search
    Then Show results

  Scenario: Use search with numbers only
    Given Open eBay.com
    And Search for 123
    And Click Search
    Then Show results

  Scenario: Use search with num, str, spec characters
    Given Open eBay.com
    And Search for dress^#$%123
    And Click Search
    Then Show results

  Scenario: Use search with space " "
    Given Open eBay.com
    And Search for " "
    And Click Search
    Then Show results




