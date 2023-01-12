from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'title',
        'description',
        'rating',
        'image',
        'review_date',
    )

    ordering = ('-review_date',)


admin.site.register(Review, ReviewAdmin)