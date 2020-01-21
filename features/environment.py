from selenium import webdriver
import os

def before_all(context):
  chrome_option = webdriver.ChromeOptions()
  if os.environ.get('docker') == 'true':
    print("Init docker env")
    chrome_option.add_argument("headless")
    chrome_option.add_argument("--no-sandbox")
    chrome_option.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(executable_path='/app/drivers/chromedriver',chrome_options=chrome_option)
  else:
    context.driver = webdriver.Chrome(executable_path='/Users/anton/Documents/qa-assignment-template/drivers/chromedriver', chrome_options=chrome_option)

  context.driver.implicitly_wait(5)

def after_all(context):
  context.driver.quit()