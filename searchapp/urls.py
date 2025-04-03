from django.urls import path
from . import views
from searchapp.views import scrape_nykaa_f
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('scrape_nykaa', scrape_nykaa_f, name="scrape_nykaa"),
]

