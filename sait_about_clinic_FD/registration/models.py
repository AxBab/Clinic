from django.db import models


class Registers(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    pol = models.CharField('Пол', max_length=10)
    age = models.CharField('Возраст', max_length=8)
    phone = models.CharField('Номер телефона', max_length=12)
    email = models.EmailField('Электронная почта', max_length=40)
    password = models.CharField('Пароль', max_length=30)


    def __str__(self):
        return  self.name + ' ' + self.surname


    class Meta:
        verbose_name = 'Пациента'
        verbose_name_plural = 'Пациенты'







