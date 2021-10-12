from django.urls import path
from .views import *


urlpatterns = [
    path('SampleEndpoint',SampleEndpoint.as_view()),
    path('QueryEndpoint',QueryEndpoint.as_view())
]
