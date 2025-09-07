import unittest
from app import app as flask_app, db, Todo

class FlaskTodoTest(unittest.TestCase):
    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with flask_app.app_context():
            db.create_all()

    def tearDown(self):
        with flask_app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task_redirects(self):
        # שינוי הנתיב מ'/' ל-'/add'
        # ושינוי מפתח הנתונים מ'task' ל-'title'
        response = self.app.post('/add', data={'title': 'Test Task'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_task_is_in_db(self):
        with flask_app.app_context():
            # שינוי הנתיב מ'/' ל-'/add'
            # ושינוי מפתח הנתונים מ'task' ל-'title'
            self.app.post('/add', data={'title': 'Another Test Task'}, follow_redirects=True)
            # שינוי שם השדה בחיפוש במסד הנתונים מ'text' או 'content' ל-'title'
            task = Todo.query.filter_by(title='Another Test Task').first()
            self.assertIsNotNone(task)

if __name__ == '__main__':
    unittest.main()