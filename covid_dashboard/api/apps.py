from django.apps import AppConfig

# in myproject/backend/backend.py or myproject/api/api.py
from .data_layer.load_csv import *


class ApiConfig(AppConfig):
	default_auto_field = "django.db.models.BigAutoField"
	name = "api"
	# data_layer = None

	# def __init__(self, app_name, app_module):
	# 	super(ApiConfig, self).__init__(app_name, app_module)
	# 	self.requests_session = None
	# 	self.data_layer_obj = None

	# loads csv at startup
	# def ready(self):
	# 	self.data_layer_obj = DataLayer()
	# 	self.data_layer_obj.initLoadCSV("api/data/archive/covid_19_data.csv")

	# def get_data_layer(self):
	# 	return self.data_layer_obj
