from selenium.webdriver.common.by import By

def test_add_product_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()  # Add first product
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert driver.find_element(By.CLASS_NAME, "cart_item").is_displayed()
