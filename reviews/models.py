from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product


# Create your models here.

class Review(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4','4'),
        ('5','5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title =  models.TextField(max_length=100)
    description = models.TextField()
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, null=True)
    image = models.ImageField(null=True, blank=True)
    review_date = models.DateTimeField(auto_now_add=True, verbose_name='Review Date') 


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"
        ordering = ['-review_date']