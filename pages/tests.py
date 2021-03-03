from django.test import SimpleTestCase
from django.urls import reverse

class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        response = slice.client.get('/')
        self.assertEqual(response.satatus_code, 200)
        def test_about_page_status_code(self):
            response = self.lient.get(reverse("about"))
            self.assertEqual(response.satatus_code, 200)

