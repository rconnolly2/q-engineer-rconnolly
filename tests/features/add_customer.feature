Feature: Bank Manager customer management

  Scenario: Add and delete a customer
    Given I am on the banking application home page
    When I log in as bank manager
    And I add a new customer
    Then the customer should appear in the customer list
    When I delete the customer
    Then the customer should be removed successfully
