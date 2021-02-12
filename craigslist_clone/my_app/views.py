import requests
from django.shortcuts import render
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from . import models

cl_base_url = "https://seattle.craigslist.org/d/services/search/bbb?query={}"
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    # turns the base url into a working link
    models.Search.objects.create(search=search)
    final_url = cl_base_url.format(quote_plus(search))
    response = requests.get(final_url)
    # gets all of the html and css from the queried url to parse
    data = response.text
    print(data)
    frontend_elements = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', frontend_elements)