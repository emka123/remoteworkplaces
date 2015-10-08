from django.shortcuts import render
from django.utils import timezone
from .models import Place

def place_list(request):
    places = Place.objects.order_by('title')
    return render(request, 'digitalnomads/place_list.html', {'places': places})

def base(request):
    return render(request, 'digitalnomads/base.html')

def about_me(request):
	return render(request, 'digitalnomads/about_me.html')