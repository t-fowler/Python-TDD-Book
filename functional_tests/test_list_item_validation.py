from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentaly tries to
        # submit, hitting ENTER on the empty input box.
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message
        # stating that items cannot be blank.
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item."
        ))

        # She tries again with some text for the item and it works.
        self.browser.find_element(By.ID, 'id_new_item').send_keys("Buy milk")
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Curious, she now tries to submit an empty list item again.
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # She receives a similar warning on the list page.
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item."
        ))

        # And she can correct it by filling some text in.
        self.browser.find_element(By.ID, 'id_new_item').send_keys("Make tea")
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

