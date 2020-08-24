from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creación user con email"""

        email = 'get.moises@gmail.com'
        password = 'Moses666'
        username = 'Hallvaror'
        genero = 'Masculino'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username,
            genero=genero
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.username, username)
        self.assertEqual(user.genero, genero)

    def test_new_user_email_normalize(self):
        """Normalizar email"""
        email = 'get.moises@GMAIL.COM'
        user = get_user_model().objects.create_user('moshe', email, 'Moses666')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test error al crear correo"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('moshe', None, 'Moses666')

    def test_create_new_superuser(self):
        """Test Crear SUPERUSER"""
        user = get_user_model().objects.create_superuser(
            'get.moises@gmail.com',
            'Moses666'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
