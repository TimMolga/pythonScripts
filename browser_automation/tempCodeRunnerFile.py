from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://github.com')

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("<email>")

password_box = browser.find_element_by_id("password")
password_box.send_keys("<password>")
password_box.submit()
