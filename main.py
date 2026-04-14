print("""
---------------------------------------------------------------------
      WELCOME TO ECO-RIDE URBAN MOBILE SYSTEM
-----------------------------------------------------------------------""")
from functions.vehicle import Vehicle,Vehicle_data
class Vehicle:
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




