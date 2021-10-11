from rest_framework import serializers

class CountrySerializer(serializers.Serializer):
	country_name = serializers.CharField()
	states = serializers.DictField()
	total_confirmed_cases = serializers.IntegerField()
	total_deaths = serializers.IntegerField()
	total_recovered = serializers.IntegerField()
	dates = serializers.ListSerializer()

class StateSerializer(serializers.Serializer):
	state_name = serializers.CharField()
	country_name = serializers.CharField()
	total_confirmed_cases = serializers.IntegerField()
	total_deaths = serializers.IntegerField()
	total_recovered = serializers.IntegerField()
	dates = serializers.ListSerializer()
	
class DateSerializers(serializers.Serializer):
	date = serializers.CharField()
