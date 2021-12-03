from django.urls import path
from .views import index

urlpatterns = [
	path("", index),
	path("Analytics", index),
	path("TextAnalytics", index),
	path("HomePage", index),
]
