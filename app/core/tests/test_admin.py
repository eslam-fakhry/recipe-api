from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='Password'
        )
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='Password',
            name="Adam Smith"
        )
        self.client.force_login(self.admin_user)

    def test_user_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        print(res)
        self.assertContains(res, self.user.name)
        # self.assertContains(res, 'game')
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test user page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that add user page is working"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
