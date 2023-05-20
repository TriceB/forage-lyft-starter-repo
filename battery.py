from abc import ABC

from car import Car
from datetime import datetime


class Battery(Car, ABC):
	def __init__(self, last_service_date, current_date):
		super().__init__(last_service_date, current_date)
		self.last_service_date = last_service_date
		self.current_date = datetime.today().date()
	
	def needs_service(self):
		service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
		if service_threshold_date < self.current_date:
			return True
		else:
			return False
		