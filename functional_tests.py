from selenium import webdriver
import unittest

#As an External researcher, I want search studies so that I can find studies that include samples of my interest
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):  #1

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_search_studies_and_select_the_result(self):
        non_defined_study ="non_defined_study"
        defined_study ="test_study"

        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('BBCatalog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('BBCatalog', header_text)

        # Follows the link to search studies
        search_link = self.browser.find_element_by_css_selector("a.search_link")
        search_link.click()
        # the new page has the word 'search' in the title
        self.assertIn('search', self.browser.title)

        # Inputs a text fro an non-existing study in the general text search
        inputbox = self.browser.find_element_by_id('text_search')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Search a study'
        )
        inputbox.send_keys(non_defined_study)
        inputbox.send_keys(Keys.ENTER)

        # There are not results for it
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertEqual(len(rows), 0)

        # inputs an existing study
        inputbox.send_keys(defined_study)
        inputbox.send_keys(Keys.ENTER)

        # there are results
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(len(rows) > 0, "there are results")

        # Chooses one of them
        rows[0].find_elements_by_tag_name('a').click()

        # the title of the found study includes
        self.assertIn(defined_study, self.browser.title)

        # Gets the needed information.
        self.fail('Finish the test!')




if __name__ == '__main__':
    unittest.main(warnings='ignore')