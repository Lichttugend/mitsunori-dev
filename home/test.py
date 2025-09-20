from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

class ContactPageTests(TestCase):
    def test_contact_page_status_code(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)