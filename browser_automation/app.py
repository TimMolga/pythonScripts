from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://github.com')

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("<username>")

password_box = browser.find_element_by_id("password")
password_box.send_keys("<password>")
password_box.submit()

assert "<username>" in browser.page_source

profile_link = browser.find_elements_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "<username>" in link_label

browser.quit()
