from django.urls import path

from extractor.views import Extractor

urlpatterns = [
    path('api/extract', Extractor.as_view(), name="ah-shit")
]
