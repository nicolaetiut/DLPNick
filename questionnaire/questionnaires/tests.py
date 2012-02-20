from django.test import TestCase
from models import Questionnaire


class AlgorithmTestCase(TestCase):
    def setUp(self):
        self.quest = Questionnaire.objects.create(name="lion", sound="roar")
        self.cat = Animal.objects.create(name="cat", sound="meow")

    def test_check_page(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(self.lion.speak(), 'The lion says "roar"')
        self.assertEqual(self.cat.speak(), 'The cat says "meow"')
