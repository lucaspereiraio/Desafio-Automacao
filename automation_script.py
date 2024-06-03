import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

def read_login_data(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row['username'], row['password']

def login_to_swag_labs(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    
    return driver

def add_items_to_cart(driver):
    items_to_add = [
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Bike Light"
    ]
    
    for item in items_to_add:
        item_button = driver.find_element(By.XPATH, f"//div[text()='{item}']/following-sibling::button")
        item_button.click()

def view_cart_and_checkout(driver):
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.ID, "first-name")
    last_name = driver.find_element(By.ID, "last-name")
    postal_code = driver.find_element(By.ID, "postal-code")

    first_name.send_keys("Lucas")
    last_name.send_keys("Pereira")
    postal_code.send_keys("71090000")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

def print_total_price(driver):
    total_price = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    print(total_price)

if __name__ == "__main__":
    username, password = read_login_data('login.csv')
    driver = login_to_swag_labs(username, password)
    add_items_to_cart(driver)
    view_cart_and_checkout(driver)
    print_total_price(driver)
    driver.quit()