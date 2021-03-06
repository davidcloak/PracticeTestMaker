from django.test import TestCase
from django.urls import resolve
from tombApp.views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    def testHomePage(self):
        found = resolve('/')#root page or webroot, no folder 127.0.0.1:8000
        self.assertEqual(found.func, home_page, 'Home page resolves incorrectly')

#check content of a home page
    def testHomePage(self):
        request = HttpRequest()
        response = home_page() #all the HTML
        html = response.content.decoe('utf8') #convert to human readable HTML
        self.assertIn('<h1>Welcome to the TOmb of Horror</h1>', html, 'H1 contents fail')
#check for player name

#check for health status

#check for...