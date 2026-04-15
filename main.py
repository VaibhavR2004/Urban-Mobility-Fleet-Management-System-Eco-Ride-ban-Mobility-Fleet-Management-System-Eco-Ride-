print("""
---------------------------------------------------------------------
      WELCOME TO ECO-RIDE URBAN MOBILE SYSTEM
-----------------------------------------------------------------------""")
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
      def __eq__(self, other):
            return self.vehicle_id==other.vehicle_id
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
      def add_vehicle(self,hub_name,vehicle):
            if hub_name not in self.hubs:
                  return f"{hub_name}, Not fount"
            existing_ids = [v.vehicle_id for v in self.hubs[hub_name]]

            if vehicle.vehicle_id in existing_ids:
                  return f"{vehicle.vehicle_id}, Duplicate Vehicle"

            self.hubs[hub_name].append(vehicle)
      def search_by_hub(self,hub_name):
            if hub_name not in self.hubs:
                  return[]
            return self.hubs[hub_name]
      def get_vehicle_battery(self):
            result=[]
            for vehicle in self.hubs.values():
                  filtered = list(filter(lambda v: v.battery_percentage > 80, vehicle))
                  result.extend(filtered)
            return result
      




fleet = Fleet_Management()


fleet.add_hub("Downtown")
fleet.add_hub("Airport")


car1 = Electric_Cars("C101", "Tesla Model 3", 90, 5)
car2 = Electric_Cars("C102", "Nissan Leaf", 70, 5)

scooter1 = Scooters("S101", "Ola S1", 85, 60)
scooter2 = Scooters("S102", "Ather 450X", 60, 80)


fleet.add_vehicle("Downtown", car1)
fleet.add_vehicle("Downtown", scooter1)

fleet.add_vehicle("Airport", car2)
fleet.add_vehicle("Airport", scooter2)


print("\nVehicles in Downtown Hub:")
for v in fleet.search_by_hub("Downtown"):
    print(v.vehicle_id, v.model, v.battery_percentage)




print("\nVehicles with Battery > 80%:")

high_battery = fleet.get_vehicle_battery()

for v in high_battery:
    print(v.vehicle_id, v.model, v.battery_percentage)



