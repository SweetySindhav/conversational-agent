from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class ActionWeather(Action):
	def name(self):
		return 'action_weather'

	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		#your apixu key from apixu
		api_key = 'e15324bff6e34eac8cb75040191105'
		client = ApixuClient(api_key)

		loc = tracker.get_slot('location')
		current = client.current(loc)
		print(current)

		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]
