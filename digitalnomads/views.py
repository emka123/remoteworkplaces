from django.shortcuts import render
from django.utils import timezone
from .models import Place

def base(request):
    places = Place.objects.order_by('title')
    return render(request, 'digitalnomads/base.html', {'places': places})

def about_me(request):
	return render(request, 'digitalnomads/about_me.html')