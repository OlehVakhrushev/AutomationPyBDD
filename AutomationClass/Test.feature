Feature: Regression for Ebay
  Background: Navifation
    Given Open eBay.com

  @bvt
  Scenario: 1: Verify that search display right items
    Given Search for "dress"
    And Click the Search button
    Then Close browser

#    Then All items are somewhat dress related
#    And Navigate to shopping cart

  @bvt
  Scenario: 2: Verify Top Bar functions (Sell)
    Given Verify that "Sell" is visible on the page
    And Click "Sell" header element
    And User is redirected to "Sell" page
    Then Close browser

  @lol
    Scenario: 3: Verify Top Bar functions (Help & Contact)
    Given Verify that "Help & Contact" is visible on the page
    And Click "Help & Contact" header element
    And User is redirected to "Help & Contact" page
    Then Close browser

  @bvt
    Scenario: 4: Verify Top Bar functions (Brand Outlet)
    Given Verify that "Brand Outlet" is visible on the page
    And Click "Brand Outlet" header element
    And User is navigated to "Brand Outlet"
    And Close browser

  @bvt
    Scenario: 5: Verify Top Bar functions (Daily Deals)
    Given Verify that "Daily Deals" is visible on the page
    And Click "Daily Deals" header element
    And User is redirected to "Daily Deals"
    And Close browser

  @bvt
  Scenario: 3: Find product and show the price
    Given Search toy product
    And Click Search
    Then Show price of first product

  @bvt
  Scenario: 4: Verify Sign In with wrong password and email
    Given Click Sign In
    And Input email
    And Click Continue
    And Input wrong password
    And Click Sign In button
    Then Verify fail

  @bvt
  Scenario: 5: Use search with srt and num
    Given Search for "dress123"
    And Click Search
    Then Show results

  @bvt
  Scenario: 6: Use search with numbers only
    Given Search for 123
    And Click Search
    Then Show results

  @bvt
  Scenario: 7: Use search with num, str, spec characters
    Given Search for "dress234#$%"
    And Click Search
    Then Show results

  @empty
  Scenario: 8: Use search with space " "
    Given Search for " "
    And Click Search
    Then Show results errors

  @bvt
  Scenario: 9: Search for Iphone 11
    Given Search Iphone 11 product
    And Click Search
    Then Show all results with Free shipping, Free returns

  @btv
  Scenario: 10: Search for Iphone 11 with Free 3 day shipping
    Given Search Iphone 11 product
    And Click Search
    Then Show all results with Free 3 day shipping

  @btv
  Scenario: 11: Search for Iphone 11 with Free 4 day shipping
#    And Show all results with Free 4 day shipping
#    And Show all results 60 Day Warranty and Charger Included
#    And Show all results with Free returns, Free 3 day shipping, 60 Day Warranty and Charger Included

  @bvt
  Scenario Outline: 12: Check if is 20 results of Iphone 11 with Free shipping and Free returns
#    Given Search Iphone 11 product
    Given In search bar type "<search_product>" from the keyboard
    And Click Search
    Then Check if results is 10
    Examples:
      | search_product |
      | Iphone 11      |

  @btv
  Scenario Outline: 13: Verify that elements are search related on pages
    Given In search bar type "<search_product>" from the keyboard
    And Click Search
    Then Verify that search results are relevant to "<search_product>" on the all pages of the search
    Examples:
      | search_product |
      | Iphone 11      |
      | dress          |
      | shoes          |
    
    
  @btv
  Scenario Outline: 14: Verify that filter is active
    Given In search bar type "<search_product>" from the keyboard
    And Click Search
    Then Filter "<search_product>" by "<filter_header>" in category "<filter_option>"
    Examples:
      | search_product |  filter_header    |  filter_option |
      | dress          |  Dress Length     |  Short         |
      | shoes          |  Brand            |  adidas        |
      | Iphone 11      |  Network          |  Sprint        |
      | books          |  Format           |  Board Book    |
      | oil            |  Originality      |  Original      |


  @btv
  Scenario Outline: 15: Multiple filter selection
    Given In search bar type "<search_product>" from the keyboard
    And Click Search
    Then Select filters
    | Filter         |  Value          |
    | <filter_name1> | <filter_value1> |
    | <filter_name2> | <filter_value2> |
    | <filter_name3> | <filter_value3> |

    Examples:
      | search_product |  filter_name1     |  filter_value1 | filter_name2  | filter_value2 | filter_name3 | filter_value3 |
      | dress          |  Dress Length     |  Short         | Sleeve Length | Sleeveless    | Brand        |  Ann Taylor   |
#
#    Examples:
#      | search_product |  filter_name1     |  filter_value1 | filter_name2 | filter_value2 |
#      | shoes          |  Brand            |  adidas        |
#      | Iphone 11      |  Network          |  Sprint        |
#      | books          |  Format           |  Board Book    |
#      | oil            |  Originality      |  Original      |


  @btv
  Scenario Outline: 17: Multiple filter selection
    Given In search bar type "<search_product>" from the keyboard
    And Click Search
    And  Select filters
    | Filter         |  Value          |
    | <filter_name1> | <filter_value1> |
    | <filter_name2> | <filter_value2> |
    | <filter_name3> | <filter_value3> |

    Examples:
      | search_product |  filter_name1     |  filter_value1 | filter_name2  | filter_value2 | filter_name3 | filter_value3 |
      | dress          |  Dress Length     |  Short         | Sleeve Length | Sleeveless    | Brand        |  Ann Taylor   |
    Then Validate what all item are related to following filters