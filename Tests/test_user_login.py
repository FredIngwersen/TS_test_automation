# Test the user login
def test_user_login(self):

    driver = self.driver

    # Goto trendsales mobile page
    driver.get('https://m.trendsales.dk/')

    self.assertIn("Trendsales", driver.title)

    # Sleep for a moment to ensure that configurations in chrome are present
    time.sleep(5)

    driver.find
