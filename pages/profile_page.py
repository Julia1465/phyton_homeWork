from selenium.webdriver.common.by import By


class ProfilePage:

   EDIT_BUTTON = (By.CSS_SELECTOR, ".user-profile__edit")
   NAME_INPUT = (By.ID, "name")
   LAST_NAME_INPUT = (By.ID, "surname")
   SAVE_PROFILE_BUTTON = (By.CSS_SELECTOR, ".gf-button.--success")
   USER_NAME_MAIN = (By.CSS_SELECTOR, "h6.mb-0")

    def __init__(self, driver, url):
    self.driver = driver
    self.url = url