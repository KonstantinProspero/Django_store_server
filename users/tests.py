from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import EmailVerification, User


# Create your tests here.
class UserRegistrationViewTestCase(TestCase):
	
	def setUp(self) -> None:
		self.data = {
			'first_name': 'Konstantin', 'last_name': 'Nikolaev',
			'username': 'kostnik', 'email': 'konstnik@gmail.com',
			'password1':'12345678Gf', 'password2':'12345678Gf',
		}
		self.path = reverse('users:registration')
	
	def test_user_registration_get(self):
		response = self.client.get(self.path)
		# print(self.path)
		
		self.assertEqual(response.status_code, HTTPStatus.OK)
		self.assertEqual(response.context_data['title'], 'Store - Регистрация')
		# print(response.context_data['title'])
		self.assertTemplateUsed(response, 'users/registration.html')
		
	def test_user_registration_post_success(self):

		username = self.data['username']
		self.assertFalse(User.objects.filter(username = username).exists())
		response = self.client.post(self.path, self.data )
		print(User.objects.filter(username = username).exists())
		# Check creating of user
		self.assertEqual(response.status_code, HTTPStatus.FOUND)
		self.assertRedirects(response, reverse('users:login'))
		self.assertTrue(User.objects.filter(username = username).exists())
		print(User.objects.filter(username = username).exists())
		
		# Check creating of email verification
		email_verificatin = EmailVerification.objects.filter(user__username=username)
		self.assertTrue(email_verificatin.exists())
		self.assertEqual(
			email_verificatin.first().expiration.date(),
			(now() + timedelta(hours = 48)).date()
		)
	
	def test_user_registration_post_error(self):
		User.objects.create(username=self.data['username'])
		response = self.client.post(self.path, self.data)
		
		self.assertEqual(response.status_code, HTTPStatus.OK)
		self.assertContains(response, 'Пользователь с таким именем уже существует.', html = True)
		