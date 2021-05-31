Feature: iPrice Footer

Scenario: Check footer links on Homepage are in HTTPS
  Given users go to iPrice Homepage
  When users go to the footers
  Then users see all footer links are in HTTPS

Scenario: Check footer links on Trends page are in HTTPS
  Given users go to iPrice Trends page
  When users go to the footers
  Then users see all footer links are in HTTPS

Scenario: Check footer links on Coupons page are in HTTPS
  Given users go to iPrice Coupons page
  When users go to the footers
  Then users see all footer links are in HTTPS