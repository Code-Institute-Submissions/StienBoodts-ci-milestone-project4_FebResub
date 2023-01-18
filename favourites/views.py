from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product

# Create your views here.

def all_favourites(request):
    """ A view to show all favourite products """
    
    favourites = Favourite.objects.all()

    context = {
        'favourites': favourites,
    }

    return render(request, 'favourites' , context)


@login_required
def add_favourite(request, product_id):
    """ Add a product as a favourite """

    product = get_object_or_404(Product, pk=product_id)
    Favourite.objects.create(user_profile=user, product=product)

    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def delete_favourite(request, product_id):
    """ Delete a favourite product """

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    
    Favourite.objects.filter(product=product, user=user).delete()

    return redirect(reverse('product_detail', args=[product.id]))
