from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    category_image = models.ImageField(upload_to='category_photo/')

    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = PhoneNumberField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_photo/')
    descriptions = models.TextField()
    owner = models.CharField(max_length=32)
    product_type = models.BooleanField()
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.product_name} - {self.price}'


