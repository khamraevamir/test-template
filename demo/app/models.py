from distutils.command.upload import upload
from django.db import models


class Product(models.Model):
    name = models.CharField('Name', max_length=256)
    price = models.IntegerField('Price', default=0)
    image = models.ImageField('Image', upload_to='products', blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    def __str__(self) :
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product', related_name='cart_products')
    quantity = models.IntegerField('Quantity', default=0)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = "Cart"

    def __str__(self) :
        return self.product.name