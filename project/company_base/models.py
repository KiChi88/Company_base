from django.db import models
import requests

class Department(models.Model):
    title = models.CharField(max_length = 500, verbose_name='Отдел')

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name  = models.CharField(max_length = 50, verbose_name='Имя')
    last_name   = models.CharField(max_length = 50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length = 50, verbose_name='Отчество')
    borth_date  = models.DateField(verbose_name='Дата рождения')
    email       = models.EmailField(verbose_name='Почта')
    phone       = models.CharField(max_length = 50, verbose_name='Телефон')
    data_start  = models.DateField(verbose_name='Дата начала работы')
    data_end    = models.DateField(blank=True, null=True, verbose_name='Дата увольнения')
    role        = models.CharField(max_length = 500, verbose_name='Должность')
    department  = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name='Отдел')

    class Meta:
        ordering = ['last_name']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def full_name(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name
    full_name.short_description = 'ФИО'

    # Праверка корректности url для тестов
    def current_url(self):
        response = requests.get(r'http://company.com/employee/' + str(self.id))
        return response.text if response.ok else 'Error'

    def __str__(self):
        return self.last_name + ' ' + self.first_name