from django.urls import path
from . import views

urlpatterns = [
    path('', views.favourites, name='favourites'),
    path('add/<int:product_id>/', views.add_favourite, name='add_favourite'),
    path('delete/<int:product_id>/', views.delete_favourite, name='delete_favourite'),
]
