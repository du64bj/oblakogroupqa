# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

@given('website "{url}"')
def step(context, url):
    context.browser = webdriver.Chrome(executable_path='/Users/anton/Documents/qa-assignment-template/drivers/chromedriver')
    context.browser.maximize_window()
    context.browser.get(url)


@then("push add new todo button")
def step(context):
    context.browser.find_element_by_id('add_new_todo').click()

@then("select add new todo list by '{value}'")
def step(context, value):
    select = Select(context.browser.find_element_by_id("select_category"));
    time.sleep(1)
    all_options = select.options
    for option in all_options:
        if option.get_attribute("value") == value:
            option.click()
            break
   
    


@then("add title for input '{text}'")
def step(context, text):
    context.browser.find_element_by_id('project_title').clear();
    time.sleep(1)
    context.browser.find_element_by_id('project_title').send_keys(text)

@then("create todo list")
def step(context):
    time.sleep(1)
    context.browser.find_element_by_id("submit_add_todo").click()

@then("close browser")
def step(context):
    time.sleep(3)
    context.browser.quit()