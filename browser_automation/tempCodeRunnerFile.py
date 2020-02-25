from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://github.com')

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("timothymolga@gmail.com")

password_box = browser.find_element_by_id("password")
password_box.send_keys("rpg3law0!")
password_box.submit()
