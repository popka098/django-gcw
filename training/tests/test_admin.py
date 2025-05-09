from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from training.admin import Task9Resource, Task10Resource, Task11Resource, Task12Resource
from training.admin import Task9Admin, Task10Admin, Task11Admin, Task12Admin
from training.models import Task9, Task10, Task11, Task12

class AdminTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@example.com'
        )
        self.client = Client()
        self.client.login(username='admin', password='admin123')
        self.admin_site = AdminSite()

    def test_task9_resource_validation(self):
        resource = Task9Resource()

        valid_row = {
            'Word': 'тест',
            'Pass': 'те.т',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertFalse(resource.skip_row(None, None, valid_row))

        empty_word_row = {
            'Word': '',
            'Pass': 'те.т',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, empty_word_row))

        empty_pass_row = {
            'Word': 'тест',
            'Pass': '',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, empty_pass_row))

        different_length_row = {
            'Word': 'тест',
            'Pass': 'те.т.',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, different_length_row))

        no_dot_row = {
            'Word': 'тест',
            'Pass': 'тест',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, no_dot_row))

        multiple_dots_row = {
            'Word': 'тест',
            'Pass': 'те.т.',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, multiple_dots_row))

    def test_task9_admin(self):
        admin = Task9Admin(Task9, self.admin_site)

        self.assertEqual(
            admin.list_display,
            ("Word", "Context_Before", "Pass", "Context_After")
        )

        self.assertEqual(
            admin.search_fields,
            ("Word", "Context_Before", "Pass", "Context_After")
        )

        self.assertEqual(admin.resource_class, Task9Resource)

    def test_task10_resource_validation(self):
        resource = Task10Resource()

        valid_row = {
            'Word': 'тест',
            'Pass': 'те.т',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertFalse(resource.skip_row(None, None, valid_row))

        empty_word_row = {
            'Word': '',
            'Pass': 'те.т',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, empty_word_row))

        empty_pass_row = {
            'Word': 'тест',
            'Pass': '',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, empty_pass_row))

        different_length_row = {
            'Word': 'тест',
            'Pass': 'те.т.',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, different_length_row))

        no_dot_row = {
            'Word': 'тест',
            'Pass': 'тест',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, no_dot_row))

        multiple_dots_row = {
            'Word': 'тест',
            'Pass': 'те.т.',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, multiple_dots_row))

    def test_task10_admin(self):
        admin = Task10Admin(Task10, self.admin_site)

        self.assertEqual(
            admin.list_display,
            ("Word", "Context_Before", "Pass", "Context_After")
        )

        self.assertEqual(
            admin.search_fields,
            ("Word", "Context_Before", "Pass", "Context_After")
        )

        self.assertEqual(admin.resource_class, Task10Resource)


    def test_task11_resource_validation(self):
        resource = Task11Resource()

        valid_row = {
            'Word': 'тест',
            'Pass': 'те.т',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertFalse(resource.skip_row(None, None, valid_row))

        empty_word_row = {
            'Word': '',
            'Pass': 'те.т',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, empty_word_row))

        empty_pass_row = {
            'Word': 'тест',
            'Pass': '',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, empty_pass_row))

        different_length_row = {
            'Word': 'тест',
            'Pass': 'те.т.',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, different_length_row))

        no_dot_row = {
            'Word': 'тест',
            'Pass': 'тест',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, no_dot_row))

        multiple_dots_row = {
            'Word': 'тест',
            'Pass': 'те.т.',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, multiple_dots_row))

    def test_task11_admin(self):
        admin = Task11Admin(Task11, self.admin_site)

        self.assertEqual(
            admin.list_display,
            ("Word", "Context_Before", "Pass", "Context_After")
        )

        self.assertEqual(
            admin.search_fields,
            ("Word", "Context_Before", "Pass", "Context_After")
        )

        self.assertEqual(admin.resource_class, Task11Resource)


    def test_task12_resource_validation(self):
        resource = Task12Resource()

        valid_row = {
            'Word': 'тест',
            'Pass': 'те.т',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertFalse(resource.skip_row(None, None, valid_row))

        empty_word_row = {
            'Word': '',
            'Pass': 'те.т',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, empty_word_row))

        empty_pass_row = {
            'Word': 'тест',
            'Pass': '',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, empty_pass_row))

        different_length_row = {
            'Word': 'тест',
            'Pass': 'те.т.',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, different_length_row))

        no_dot_row = {
            'Word': 'тест',
            'Pass': 'тест',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, no_dot_row))

        multiple_dots_row = {
            'Word': 'тест',
            'Pass': 'те.т.',
            'Context_Before': 'перед',
            'Context_After': 'после'
        }
        self.assertTrue(resource.skip_row(None, None, multiple_dots_row))

    def test_task12_admin(self):
        admin = Task12Admin(Task12, self.admin_site)

        self.assertEqual(
            admin.list_display,
            ("Word", "Context_Before", "Pass", "Context_After")
        )

        self.assertEqual(
            admin.search_fields,
            ("Word", "Context_Before", "Pass", "Context_After")
        )

        self.assertEqual(admin.resource_class, Task12Resource)


    def test_admin_interface_access(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/admin/training/task9/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/admin/training/task9/add/')
        self.assertEqual(response.status_code, 200)
