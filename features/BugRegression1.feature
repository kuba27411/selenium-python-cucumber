Feature: Wrong color on a button (BUG) 
  This feature is a regression feature from one of the UI bugs that I found and its expected to fail until the bug is fixed.
  expected error: Assertion Failed: Expected button color to be #ffffff but was rgb(0, 0, 0)

  Scenario: Checking a color of an element (BUG) 
    When visiting website
    Then waits until element is visible then clicks the element by xpath "//*[@id="pa_5c9126fe3b767_p15577f075e9-textButton"]"
    Then waits until element is visible then clicks the element by xpath "//*[@id='pa_5c9126fe3f4fb_p179d7b273e1-card__image-1']"
    Then waits until element is visible then clicks the element by xpath "//*[@id="pa_5c9126fe434ba_p15564daa856-textButton"]"
    Then waits until element is visible then clicks the element by xpath "//*[@id="pa_5c9126fe47260_p15515116385-itemInner-1"]/span[2]"
    Then waits until element is visible then clicks the element by xpath "//*[@id="pa_5c9126fe47260_p15515116385-button__text"]"
    Then waits until element is visible then clicks the element by xpath "//*[@id="pa_5c9126fe47260_p15583b88249-dismiss_button"]"
    Then waits until element is visible then clicks the element by xpath "//*[@id="pa_5c9126fe4b742_p15550a254a1-textButton"]"
    Then the button color should be "#ffffff" for xpath "//*[@id="pa_5c9126fe4b742_p15550a254a1-textButton"]"
    Then wait for 5 seconds