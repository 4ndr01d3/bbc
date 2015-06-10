from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.core.urlresolvers import resolve
from bbc.views import home_page, study
from bbc.models import Study, Biobank


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)



class StudyTest(TestCase):
    def test_adding_study_to_the_model(self):
        defined_study = 'a_study_name'

        biobank = Biobank.objects.create()
        to_add = Study.objects.create(name=defined_study, biobank=biobank)

        self.assertEqual(Study.objects.count(), 1)
        new_item = Study.objects.first()
        self.assertEqual(new_item.name, to_add.name)

    def test_study_page_displays_all_searched_items(self):
        biobank = Biobank.objects.create()
        Study.objects.create(name='itemey 1', biobank=biobank)
        Study.objects.create(name='itemey 2', biobank=biobank)

        response = self.client.get("/study/", {"text_search":"itemey"})

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_study_template(self):
        biobank = Biobank.objects.create()
        study = Study.objects.create(name='itemey 1', biobank=biobank)
        response = self.client.get('/study/{}/'.format(study.id))
        self.assertTemplateUsed(response, 'study.html')

class BiobankTest(TestCase):
    def test_biobank_page_list_all_biobanks(self):
        biobank1 = Biobank.objects.create(name="bb1")
        biobank2 = Biobank.objects.create(name="bb2")
        response = self.client.get("/biobank/")
        self.assertContains(response, biobank1.name)
        self.assertContains(response, biobank2.name)
        self.assertNotContains(response, "bb3")

    def test_biobank_page_list_its_studies(self):
        biobank = Biobank.objects.create()
        Study.objects.create(name='itemey 1', biobank=biobank)
        Study.objects.create(name='itemey 2', biobank=biobank)
        response = self.client.get("/biobank/{}/".format(biobank.id))
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


class ModelTest(TestCase):

    def test_saving_and_retrieving_studies(self):
        biobank = Biobank()
        biobank.save()

        first_study = Study()
        first_study.name = 'test_study'
        first_study.biobank = biobank
        first_study.save()

        second_study = Study()
        second_study.name = 'second_test'
        second_study.biobank = biobank
        second_study.save()

        saved_studies = Study.objects.all()
        self.assertEqual(saved_studies.count(), 2)

        first_saved_item = saved_studies[0]
        second_saved_item = saved_studies[1]
        self.assertEqual(first_saved_item.name, 'test_study')
        self.assertEqual(first_saved_item.biobank, biobank)
        self.assertEqual(second_saved_item.name, 'second_test')
        self.assertEqual(second_saved_item.biobank, biobank)

    def test_saving_and_retrieving_biobanks(self):
        biobank = Biobank.objects.create(name="biobank")

        saved_bb = Biobank.objects.first()
        self.assertEqual(saved_bb, biobank)

