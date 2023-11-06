from django.db import models


class Product(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    supplier = models.CharField(max_length=100, verbose_name='поставщик')
    debt = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    get_supplier_link = models.URLField(verbose_name='ссылка на поставщика')

    def __str__(self):
        return f'{self.name_product}, {self.model}, {self.release_date}, {self.get_supplier_link}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Suppliers(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')
    supplier = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='поставщик')

    def __str__(self):
        return f'{self.name}, {self.country}, {self.supplier}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
