#Feature: Hello world
#
# Scenario: Test
#   Given Navigate to Google

Feature: Regression for Ebay

  Scenario: Verify that search display right items
    Given Open eBay.com
    And Search for "dress"
    And Click the Search button
    Then All items are somewhat dress related