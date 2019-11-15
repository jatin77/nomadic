from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import city_choice, country_choice, nomad_price

from listings.models import Listing
from guides.models import Guide

def index(request):
    listings = Listing.objects.order_by('-city')[:3]
    context = {
        'listings':listings,
        'city_choice':city_choice,
        'country_choice':country_choice,
        'nomad_price':nomad_price
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all Guides
    guides = Guide.objects.all()

    # Get mvp
    mvp_guide = Guide.objects.all().filter(id=2)

    context = {
        'guides':guides,
        'mvp_guides':mvp_guide
    }

    return render(request, 'pages/about.html', context)
