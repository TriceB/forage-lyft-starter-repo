from abc import ABC

from car import Car


class Engine(Car, ABC):
	def __init__(self, current_mileage, last_service_mileage, warning_light_is_on):
		super().__init__(current_mileage, last_service_mileage)
		self.warning_light_is_on = warning_light_is_on
		self.current_mileage = current_mileage
		self.last_service_mileage = last_service_mileage
	
	def needs_service(self):
		if self.warning_light_is_on or self.current_mileage - self.last_service_mileage > 60000:
			return True
		else:
			return False




