from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith wants to try out a new, online to-do list app. She goes
        # to check out the home page.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test.')

        # She is invited to enter a to-do item right away.

        # She types "buy peacock feathers" into the text box.

        # When she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list.

        # There is still a text box, inviting her to add another item. She
        # enters "Make peacock feather flies".

        # The page updates again, now showing both items on the list.

        # Edith wonders whether the site will remember her list. The
        # page explains that her list has been generated a unique URL.

        # She visits the unique URL, and her to-do list is still there.

if __name__ == "__main__":
    unittest.main()
