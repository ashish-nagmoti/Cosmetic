from django.shortcuts import render
from .scrapper import scrape_nykaa, scrape_amazon, scrape_tira

def index(request):
    return render(request, 'index.html')

def results(request):
    query = request.GET.get('q', '')
    products = []
    if query:
        products.extend(scrape_nykaa(query))
        products.extend(scrape_amazon(query))
        #products.extend(scrape_tira(query))
        # Optional: sort or deduplicate the combined results here.
    
    context = {
        'query': query,
        'products': products,
    }
    return render(request, 'result.html', context)
