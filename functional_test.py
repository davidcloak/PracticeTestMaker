from selenium import webdriver
import unittest
#make sure website and server are working
#big picture testing
class FunctionalTest(unittest.TestCase):
    def setUp(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.headless = True
        fireFoxOptions.headless = True
        #self.browser = webdriver.Firefox(options=fireFoxOptions)
        self.browser = webdriver.Firefox()
        self.browser.get('http://127.0.0.1:8000')
    
    def tearDown(self):
        #self.browser.quit()


    #@unittest.SkipTest #ignore a test
    def test_title(self):
        self.assertIn('Django', self.browser.title, 'Wrong Title')

if __name__ == '__main__':
    #calls the class if it is not instantiated elsewhere
    unittest.main()