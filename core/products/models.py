from django.db import models
from base.models import *
from django.utils.text import slugify


# Create your models here.
class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='category')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name


class Product(BaseModel):
    product_name = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='products')
    price = models.IntegerField()
    product_description = models.TextField()

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name
        
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product')

    def __str__(self) -> str:
        return str(self.product)
