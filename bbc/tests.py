from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve
from bbc.views import home_page, study
from bbc.models import Study


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


class StudyTest(TestCase):
    def test_study_page_can_search_with_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        defined_study = 'a_study_name'
        request.POST['text_search'] = defined_study

        to_add = Study()
        to_add.name = defined_study
        to_add.save()

        response = study(request)

        self.assertEqual(Study.objects.count(), 1)  #1
        new_item = Study.objects.first()  #2
        self.assertEqual(new_item.name, defined_study)  #3

    def test_study_page_displays_all_searched_items(self):
        Study.objects.create(name='itemey 1')
        Study.objects.create(name='itemey 2')

        request = HttpRequest()
        request.method = 'POST'
        request.POST['text_search'] = 'itemey'

        response = study(request)

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class StudyModelTest(TestCase):

    def test_saving_and_retrieving_studies(self):
        first_study = Study()
        first_study.name = 'test_study'
        first_study.save()

        second_study = Study()
        second_study.name = 'second_test'
        second_study.save()

        saved_studies = Study.objects.all()
        self.assertEqual(saved_studies.count(), 2)

        first_saved_item = saved_studies[0]
        second_saved_item = saved_studies[1]
        self.assertEqual(first_saved_item.name, 'test_study')
        self.assertEqual(second_saved_item.name, 'second_test')

