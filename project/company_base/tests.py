from django.test import TestCase
from unittest.mock import patch
from .models import Employee
import datetime

class EmployeeTest(TestCase):

    def setUp(self):
        self.emp = Employee(first_name='Тестер', 
                   last_name='Тестеров', 
                   middle_name='Петрович', 
                   borth_date=datetime.datetime(1960, 1, 12), 
                   email='mail.mail@mail.ru',
                   phone='+ 7 (111) 111-11-11', 
                   data_start=datetime.datetime(1990, 5, 12),
                   data_end=datetime.datetime(1991, 1, 12), 
                   role='Сотрудник', 
                   department_id=10)

    def test_create(self):
        self.assertTrue(isinstance(self.emp, Employee))

    def test_full_name(self):
        self.assertEqual('Тестеров Тестер Петрович', self.emp.full_name())

    def test_current_url(self):
        with patch('company_base.models.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            current_url = self.emp.current_url()
            mocked_get.assert_called_with('http://company.com/employee/' + str(self.emp.id))
            self.assertEqual(current_url, 'Success')

            mocked_get.return_value.ok = False

            current_url = self.emp.current_url()
            mocked_get.assert_called_with('http://company.com/employee/' + str(self.emp.id))
            self.assertEqual(current_url, 'Error')
