from abc import ABC

from car import Car

"""
  -----------------------  Original Code  -------------------------
class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
"""


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def needs_service(self):
        if self.warning_light_is_on:
            return True
        elif self.current_mileage - self.last_service_mileage > 60000:
            return True
        else:
            return False
        
        
