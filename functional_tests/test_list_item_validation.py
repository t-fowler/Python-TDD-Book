from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentaly tries to
        # submit, hitting ENTER on the empty input box.

        # The home page refreshes, and there is an error message
        # stating that items cannot be blank.

        # She tries again with some text for the item and it works.

        # Curious, she now tries to submit an empty list item again.

        # She receives a similar warning on the list page.

        # And she can correct it by filling some text in.
        self.fail('write me.')
