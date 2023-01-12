from django.shortcuts import render

def reviews(request):
    """ A view to return reviews for the producst """
    return render(request, "reviews/reviews.html")

