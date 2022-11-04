import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = '142d4ec4c74ed054ee0201eb0340a89c'
    name = 'Karaganda'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={name}&units={"metric"}&appid={appid}'

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        # form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&units={"metric"}&appid={appid}'
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        print(res)
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)

