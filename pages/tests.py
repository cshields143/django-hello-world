from django.test import SimpleTestCase

# Create your tests here.

class PagesTests(SimpleTestCase):
    def test_home_page_status_code(self):
        rsp = self.client.get('/')
        self.assertEqual(rsp.status_code, 200)
    def test_about_page_status_code(self):
        rsp = self.client.get('/about/')
        self.assertEqual(rsp.status_code, 200)
