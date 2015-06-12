from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

class NewVisitorTest(StaticLiveServerTestCase):  #1

    @classmethod
    def setUpClass(cls):  #1
        for arg in sys.argv:  #2
            if 'liveserver' in arg:  #3
                cls.server_url = 'http://' + arg.split('=')[1]  #4
                return  #5
        super().setUpClass()  #6
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.browser.get(self.server_url+"?testing=create")

    def tearDown(self):
        self.browser.get(self.server_url+"?testing=remove")
        self.browser.quit()

    #As an External researcher, I want search studies so that I can find studies that include samples of my interest
    def test_can_search_studies_and_select_the_result(self):
        # setting things up
        non_defined_study ="non_defined_study"
        defined_study ="study1"
        study_link="a.studies_link"

        # to check out its homepage
        self.browser.get(self.server_url)
        # She notices the page title and header mention BBCatalog
        self.assertIn('BBCatalog', self.browser.title)
        header_text = self.browser.find_element_by_css_selector('a.navbar-brand').text
        self.assertIn('BBCatalog', header_text)

        # Follows the link to studies
        search_link = self.browser.find_element_by_css_selector(study_link)
        search_link.click()
        # the new page has the word 'Studies' in the title
        self.assertIn('Studies', self.browser.title)

        # The search field has a place holder indicating is to search studies
        inputbox = self.browser.find_element_by_id('text_search')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Search a study'
        )

        # Inputs a text for an non-existing study in the general text search
        inputbox.send_keys(non_defined_study)
        inputbox.send_keys(Keys.ENTER)

        # There are not results for it
        try:
            table = self.browser.find_element_by_id('result_table')
            self.fail("it shouldn't be creating a result table")
        except:
            pass

        # The result page follows the URL pattern for searches
        new_url = self.browser.current_url
        self.assertRegex(new_url, '/study/\?text_search=.+')

        # inputs an existing study
        inputbox = self.browser.find_element_by_id('text_search')
        inputbox.send_keys(defined_study)
        inputbox.send_keys(Keys.ENTER)

        # there are results
        table = self.browser.find_element_by_id('result_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertGreater(len(rows), 0)

        # Chooses one of them
        rows[0].find_elements_by_tag_name('a')[0].click()

        new_url = self.browser.current_url
        self.assertRegex(new_url, '/study/.+')

        # the page of the found study includes the searched term
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn(defined_study, body_text)

        # Search for another unexisting study
        inputbox = self.browser.find_element_by_id('text_search')

        # Inputs a text for an non-existing study in the general text search
        inputbox.send_keys(non_defined_study)
        inputbox.send_keys(Keys.ENTER)

        # There are not results for it
        try:
            table = self.browser.find_element_by_id('result_table')
            self.fail("it shouldn't be creating a result table")
        except:
            pass
        # Gets the needed information.
        # self.fail('Finish the test!')

    def test_can_list_biobanks_select_one_and_link_to_studies(self):
        # A user goes to the home page
        self.browser.get(self.server_url)

        # Notices the link for biobanks and click on it
        search_link = self.browser.find_element_by_css_selector("a.biobanks_link")
        search_link.click()

        # The new page has the word biobanks in the title
        self.assertIn('Biobanks', self.browser.title)

        # The new page has a list of the biobanks
        ul = self.browser.find_element_by_css_selector('ul.biobank_list')
        rows = ul.find_elements_by_tag_name('li')
        self.assertEqual(len(rows), 2, "The system should have 2 biobanks")

        # The user clicks on the first biobank
        rows[0].find_elements_by_tag_name('a')[0].click()

        # The new page has the rigth URL
        new_url = self.browser.current_url
        self.assertRegex(new_url, '/biobank/.+')

        # the page of the selected biobank includes its name
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn("biobank1", body_text)
        # but doesn't include the other biobank
        self.assertNotIn("biobank2", body_text)

        # The page includes the 2 studies in the bank
        self.assertIn("study1", body_text)
        self.assertIn("study2", body_text)
        # but does not include the other 2
        self.assertNotIn("study3", body_text)
        self.assertNotIn("study4", body_text)

        # The user clicks on the first study
        self.browser.find_element_by_css_selector('a.study_link').click();

        # The page opened has the information of the study
        new_url = self.browser.current_url
        self.assertRegex(new_url, '/study/.+')

        # the page of the found study includes the searched term
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn("study1", body_text)
        self.assertNotIn("study2", body_text)

    def test_layout_and_styling(self):
        # The user goes to the home page
        self.browser.get(self.server_url)

        # and notices that there is a top navigation bar
        bar = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual(bar.value_of_css_property("position"),
                         "relative",
                         "This might indicate that the css is not loading properly");
