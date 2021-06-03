Feature: GoRewards Homepage Section

  Scenario: Verify GoRewards are up
    Given the base url is "https://gorewards.iprice.ph/"
    When I open the site "/computing/laptops/"
    Then I expect that the url is "https://gorewards.iprice.ph/computing/laptops/"
    And I expect that the title is "Go Rewards"



  Scenario Outline: Verify GoRewards section in Homepage
    Given user goes to GoRewards Homepage
    When user inspects the sections on GoRewards Homepage
    Then user sees <sections> is visible

    Examples:
      | sections          |
      | "Categories"      |
      | "Popular Today"   |
      | "Featured Brands" |