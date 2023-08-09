import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


CONTENT = settings.BUS_STATION_CSV
with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = list(csv.DictReader(csvfile))
    # for row in reader:
    #     print(row['Name'], row['Street'], row['District'])


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(reader, 10)
    current_list = paginator.get_page(page_number)
    current_page = paginator.page(page_number)

    context = {
        'bus_stations': current_list,
        'page': current_page,
    }
    return render(request, 'stations/index.html', context)
