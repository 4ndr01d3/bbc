from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve
from bbc.views import home_page, study

class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_study_page_returns_correct_html(self):
        request = HttpRequest()
        response = study(request)
        expected_html = render_to_string('study.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_study_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['text_search'] = 'A text to search'

        response = study(request)

        self.assertIn('A text to search', response.content.decode())
        expected_html = render_to_string(
            'study.html',
            {'text_search':  'A text to search'}
        )
        self.assertEqual(response.content.decode(), expected_html)
