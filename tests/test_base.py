# Flask
from flask_testing import TestCase
from flask import current_app, url_for
# App
from main import app

# TestCase HelloWorld
class MainTest(TestCase):

    # Tests about app
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        """
        ** Test if app is not None **
        """
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        """
        ** Test if app is in test mode **
        """
        self.assertTrue(current_app.config['TESTING'])

    # Tests about index path
    def test_index_redirects(self):
        """
        ** Test if from index path redirects to hello path **
        """
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))

    # Tests about hello path
    def test_hello_get(self):
        """
        ** Test if hello path with "http get method" responds with status code 200 **
        """
        response = self.client.get(url_for('hello'))
        self.assert200(response)

    def test_hello_post(self):
        """
        ** Test if hello path with "http post method" responds with redirect to index path **
        """
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)
        self.assertRedirects(response, url_for('index'))
