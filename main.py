print("""
---------------------------------------------------------------------
      WELCOME TO ECO-RIDE URBAN MOBILE SYSTEM
-----------------------------------------------------------------------""")
from functions.vehicle import Vehicle,Vehicle_data
from abc import ABC, abstractmethod
class Vehicle(ABC):
      def __init__(self,vehicle_id,model,battery_percentage):
            self.vehicle_id=vehicle_id
            self.model=model
            self.battery_percentage= battery_percentage
            self.__maintenance_status="Available"
            self.__rental_price=0
      @property
      def get_maintenance(self):
            return f"{self.vehicle_id} maintenance is {self.__maintenance_status}"

      @property
      def get_rental(self):
            return f"{self.vehicle_id} rental price {self.__rental_price}"

      def get_batter(self):
            return f"{self.vehicle_id} battery is {self.battery_percentage}%"

      def setter_battery(self,battery_percentage):
            if 0<=battery_percentage<=100:
                  self.battery_percentage=battery_percentage
            else:
                  raise ValueError("Battery must be between 0 and 100")
      @abstractmethod
      def calculate_trip_cost(self,distance):
            pass
class Electric_Cars(Vehicle):
      def __init__(self, vehicle_id, model, battery_percentage,seating_capacity):
            super().__init__(vehicle_id, model, battery_percentage)
            self.seating_capacity=seating_capacity
      
      def calculate_trip_cost(self, distance):
            self.distance=distance
            total = 5 + 0.5*(self.distance)
            return f"Total trip coast :{total:.2f}"
class Scooters(Vehicle):
      def __init__(self, vehicle_id, model, battery_percentage,max_speed_limit):
            super().__init__(vehicle_id, model, battery_percentage)
            self.max_speed_limit=max_speed_limit
      def calculate_trip_cost(self, time):
            self.time=time
            total = 1 + 0.15*(self.time)
            return f"Total trip coast :{total:.2f}"

class Fleet_Management:
      def __init__(self):
            self.hubs={}
      def add_hub(self,hub_name):
            if hub_name not in self.hubs:
                  self.hubs[hub_name]=[]
      def add_vehicle(self,hub_name,vehicle_name):
            if hub_name not in self.hubs:
                  return f"{hub_name}, Not fount"
            elif vehicle_name in self.hubs[hub_name]:
                  return f"{vehicle_name}, Already Exist"
            else:
                  self.hubs[hub_name]=vehicle_name
            


