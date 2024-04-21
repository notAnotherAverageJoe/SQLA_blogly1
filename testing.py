import unittest
from app import app, db, User

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///blogly_test"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['WTF_CSRF_ENABLED'] = False

        self.app = app.test_client()

        # Initialize the database
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Clean up the database after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_root(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_users_index(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)  # Successful response

    def test_users_new_form(self):
        response = self.app.get('/users/new')
        self.assertEqual(response.status_code, 200)  # Successful response

    def test_users_new(self):
        response = self.app.post('/users/new', data={
            'first_name': 'John',
            'last_name': 'Doe',
            'image_url': 'https://example.com/john.jpg'
        })
        self.assertEqual(response.status_code, 302)  # Redirect status code

if __name__ == '__main__':
    unittest.main()
