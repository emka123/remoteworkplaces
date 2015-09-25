
from django.shortcuts import render

def place_list(request):
    places = Place.objects.order_by('title')
    return render(request, 'digitalnomads/place_list.html', {'places': places})
