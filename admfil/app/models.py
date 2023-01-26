from django.db import models


class PC(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'ПК'
        verbose_name_plural = 'ПК'

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=255, verbose_name='Адрес')
    zipcode = models.CharField(max_length=10, verbose_name='Индекс')
    city = models.CharField(max_length=255, verbose_name='Город')
    state = models.CharField(max_length=2, verbose_name='Номер')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.street


class Person(models.Model):
    name = models.CharField(verbose_name='Информация', max_length=255)
    business_addr = models.ForeignKey(Address, verbose_name='Рабочий адрес', related_name='business_addr',
                                      on_delete=models.PROTECT)
    home_addr = models.OneToOneField(Address, verbose_name='Городской адрес', related_name='home_addr',
                                     on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Человек'

    def __str__(self):
        return self.name
