from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Review
from .models import Product
from .forms import ReviewForm

# Create your views here.

def reviews(request):
    """ A view to show all reviews """
    
    reviews = Review.objects.all()
    query = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('reviews'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            reviews = reviews.filter(queries)

    context = {
        'reviews': reviews,
        'search_term': query,
    }

    return render(request, 'reviews/reviews.html', context)


def review_detail(request, product_id):
    """ A view to show specific product reviews """
    
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    context = {
        'reviews': reviews,
        'product': product,
    }
    
    return render(request, 'review/product_reviews.html', context)

@login_required
def add_review(request):
    """ Add a review to the store """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you need to be logged in to leave a review.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('review_detail', args=[review.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()
        
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_review(request, review_id):
    """ Edit a review in the store """

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('review_detail', args=[review.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.title}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)

@login_required
def delete_review(request, review_id):
    """ Delete a review from the store """

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')

    return redirect(reverse('reviews'))
