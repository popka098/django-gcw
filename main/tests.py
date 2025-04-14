from django.test import TestCase, Client
class BasicTest(TestCase):
    # fixtures = ["db.json"]
    def setUp(self):
        self.client = Client()
        # self.client.login(username="root", password="root")
    def test_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code,200)

    # def test_logout(self):
    #     response = self.client.get('/logout/')
    #     self.assertEqual(response.status_code, 200)

    def test_reg(self):
        response = self.client.get('/registration/')
        self.assertEqual(response.status_code, 200)

