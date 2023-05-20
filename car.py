from abc import ABC, abstractmethod
from datetime import datetime
"""
  -----------------------  Original Code  -------------------------
class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
"""


class Car(ABC):
    def __init__(self, engine, battery, tire, last_service_date, current_mileage, last_service_mileage,
                 warning_light_is_on):
        self.engine = engine
        self.battery = battery
        self.tire = tire
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_is_on = warning_light_is_on
        
    @abstractmethod
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if self.warning_light_is_on or self.current_mileage - self.last_service_mileage > 60000 or service_threshold_date < datetime.today().date():
            return True
        else:
            return False
    
    def create_car(self):
        pass
