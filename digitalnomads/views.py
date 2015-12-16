from django.shortcuts import render
from django.utils import timezone
from .models import Place
from django.shortcuts import render, get_object_or_404

def base(request):
    places = Place.objects.order_by('title')
    return render(request, 'digitalnomads/base.html', {'places': places})

def about_me(request):
	return render(request, 'digitalnomads/about_me.html')

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'digitalnomads/place_detail.html', {'place': place})

def navigation(request):
    return render(request, 'navigation.html')