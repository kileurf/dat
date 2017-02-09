from django.test import TestCase
from .models import *
from django.db import IntegrityError
from datetime import date

_name="Client"
_create_date="2017-01-26"
_email="test@test.fr"

class ClientsTest(TestCase):
    def test_create_client(self):
	client1 = Client.objects.create(name=_name, create_date=_create_date, email=_email)
        self.assertEqual(client1.name, _name)

    def test_duplicate_client(self):
        with self.assertRaises(Exception) as raised:
            client1 = Client.objects.create(name=_name, create_date=_create_date, email=_email)
            client2 = Client.objects.create(name=_name, create_date=_create_date, email=_email)
        self.assertEqual(IntegrityError, type(raised.exception))
