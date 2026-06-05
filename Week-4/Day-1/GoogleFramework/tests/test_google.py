import unittest

from config.config import URL, SEARCH_TEXT
from pages.google_page import GooglePage
from utilities.browser_utils import BrowserUtils

class TestGoogle(unittest.TestCase):
    """
    The core purpose of embedding a Selenium test case inside a unit testing framework 
    (like Python's unittest or pytest) is to gain access to assertion tools, structured test reporting,
      and test lifecycle management.Selenium on its own can only control a browser (click, type, navigate);
        it cannot determine if a test passed or failed, nor can it generate automated test reports.

        Selenium can find a heading on a page, but it cannot validate it. Unit testing provides validation functions 
        like assertEqual() or assertTrue() to check if the actual webpage matches the expected design.

        Frameworks provide structural hooks like setUp() and tearDown(). This guarantees that a fresh browser opens before every single test 
        and cleanly closes afterward, even if a test crashes midway.
    """

    def setUp(self):

        self.driver = BrowserUtils.get_driver()

        self.driver.get(URL)

    def test_google_search(self):

        page = GooglePage(self.driver)

        page.search(SEARCH_TEXT)

        self.assertIn(
            "Google",
            self.driver.title
        )

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()