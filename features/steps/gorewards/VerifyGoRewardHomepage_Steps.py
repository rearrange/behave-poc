from behave import *
from behave_webdriver.steps import *


@given('user goes to GoRewards Homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user goes to GoRewards Homepage')


@when('user inspects the sections on GoRewards Homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user inspects the sections on GoRewards Homepage')


@then('user sees "Categories" is visible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user sees "Categories" is visible')


@then('user sees "Popular Today" is visible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user sees "Popular Today" is visible')


@then('user sees "Featured Brands" is visible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user sees "Featured Brands" is visible')

