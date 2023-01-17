from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product


# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title =  models.TextField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5)], null=True)
    image = models.ImageField(null=True, blank=True)
    review_date = models.DateTimeField(auto_now_add=True, verbose_name='Review Date') 


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"
        ordering = ['-review_date']