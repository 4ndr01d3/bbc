from django.test import TestCase
from django.core.urlresolvers import resolve
from bbc.views import home_page

class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)