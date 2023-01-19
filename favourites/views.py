from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile
from .models import Favourite

# Create your views here.

def favourites(request):
    """ A view to show all favourite products """
    
    user = get_object_or_404(User, user=request.user)
    favourites = Favourite.objects.filter(user=user)

    context = {
        'favourites': favourites,
    }

    return render(request, 'favourites.html', context)


@login_required
def add_favourite(request, product_id):
    """ Add a product as a favourite """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)

    Favourite.objects.create(user=user, product=product)

    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def delete_favourite(request, product_id):
    """ Delete a favourite product """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    
    Favourite.objects.filter(product=product, user=user).delete()

    return redirect(reverse('product_detail', args=[product.id]))
