from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


@given('users go to iPrice Homepage')
def users_go_to_iprice_homepage(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://iprice.my")
    context.driver.maximize_window()


@when('users go to the footers')
def users_go_to_footers(context):
    footer = context.driver.find_element_by_id("international")
    action = ActionChains(context.driver)
    action.move_to_element(footer).perform()


@then('users see all footer links are in HTTPS')
def users_see_all_footer_links_are_in_https(context):
    # International link - first country
    first_cc = context.driver.find_element_by_xpath("//*[@id='international']/ul/li[1]/a")
    first_cc.click()
    assert "https" in context.driver.current_url
    context.driver.close()


@given(u'users go to iPrice Trends page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://iprice.my/trends")
    context.driver.maximize_window()


@given(u'users go to iPrice Coupons page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://iprice.my/coupons")
    context.driver.maximize_window()
