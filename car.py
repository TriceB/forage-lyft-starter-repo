
from serviceable import Serviceable
"""
  -----------------------  Original Code  -------------------------
class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
"""


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        # self.tire = tire

    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
    
    def create_car(self):
        pass
