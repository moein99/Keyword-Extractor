from django.urls import path

from extractor.views import Extractor, ExtractorGUI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/extract', Extractor.as_view(), name="api"),
    path('gui/extract', ExtractorGUI.as_view(), name="gui"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
