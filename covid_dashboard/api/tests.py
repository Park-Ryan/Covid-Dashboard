from django.test import TestCase
from .util import *
# Create your tests here.

#true = 1, false = 0
class CountryTestCase(TestCase):
    def test_find_US(self):
        self.assertEqual(Find_Country("US"), 1)
    
    def test_find_fake_country(self):
        self.assertEqual(Find_Country("Gawr"), 0)

    def test_find_all_countries(self):
        self.assertEqual(Find_Country("Hong Kong"), 1)
        self.assertEqual(Find_Country("Macau"), 1)
        self.assertEqual(Find_Country("Taiwan"), 1)
        self.assertEqual(Find_Country("Japan"), 1)
        self.assertEqual(Find_Country("Thailand"), 1)
        self.assertEqual(Find_Country("South Korea"), 1)
        self.assertEqual(Find_Country("Singapore"), 1)
        self.assertEqual(Find_Country("Philippines"), 1)
        self.assertEqual(Find_Country("France"), 1)
        self.assertEqual(Find_Country("Mexico"), 1)
        self.assertEqual(Find_Country("Brazil"), 1)
        self.assertEqual(Find_Country("Canada"), 1)

    def test_find_State_California(self):
        self.assertEqual(Find_State("US", "California"), 1)

    def test_find_fake_state(self):
        self.assertEqual(Find_State("US", "Hololive"), 1)

    def test_find_States(self):
        self.assertEqual(Find_State("US", "Nevada"), 1)
        self.assertEqual(Find_State("Canada", "Alberta"), 1)
        self.assertEqual(Find_State("Mexico", "Jalisco"), 1)
        self.assertEqual(Find_State("Iceland", ""), 1)
        self.assertEqual(Find_State("Netherlands", "Flevoland"), 1)
    
    def test_add_country(self):
        Create_Csv("Hololive", "Gawr Gura", "Confirmed", "01/12/2021", "12")
        self.assertEqual(Find_Country("Hololive"), 1)
        self.assertEqual(Find_State("Hololive", "Gawr Gura"), 1)
        self.assertEqual(Find_State("Hololive", "Watson"), 0)

    def test_update_country(self):
        self.assertEqual(Find_Cases("US", "California", "Confirmed", "05/18/2020"), "82259.0") 
        Update_Csv("US", "California", "Confirmed", "05/18/2020", "90000000.0")
        self.assertEqual(Find_Cases("US", "California", "Confirmed", "05/18/2020"), "90000000.0") 
