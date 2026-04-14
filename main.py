print("""
---------------------------------------------------------------------
      WELCOME TO ECO-RIDE URBAN MOBILE SYSTEM
-----------------------------------------------------------------------""")
# from functions.vehicle import Vehicle,Vehicle_data
from abc import ABC, abstractmethod
class Vehicle:
      def __init__(self,vehicle_id,model,battery_percentage):
            self.vehicle_id=vehicle_id
            self.model=model
            self.battery_percentage= battery_percentage