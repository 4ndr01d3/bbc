from selenium import webdriver
import unittest

#As an External researcher, I want search studies so that I can find studies that include samples of my interest
class NewVisitorTest(unittest.TestCase):  #1

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_search_studies_and_select_the_result(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('BBCatalog', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # Follows the link to search studies

        # Inputs a complicated text in the general text search

        # There are not results for it

        # chooses some parameters from the form

        # there are results

        # Chooses one of them

        # Gets the needed information.




if __name__ == '__main__':
    unittest.main(warnings='ignore')