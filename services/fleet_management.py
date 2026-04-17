from models.vehicle import Vehicle
from models.Scooters import Scooters
from models.Electric_Cars import Electric_Cars

class Fleet_Management:
    def __init__(self):
        self.hubs={}
        self.type={}
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
    def get_vehicle_type(self):
            vehicle_type={}
            for vehicle in self.hubs.values():
                for v in vehicle:
                        if isinstance(v,Electric_Cars):
                            vehicle_type.setdefault("Car",[]).append(v)
                        elif isinstance(v,Scooters):
                            vehicle_type.setdefault("Scooter",[]).append(v)
            return vehicle_type
    def display_vehicle_type(self):
            categorized = self.get_vehicle_type()

            for category, vehicles in categorized.items():
                        print(f"{category}:")
                        for v in vehicles:
                            print(f"  {v.vehicle_id},{v.model}")
    def total_count_maintenance(self):
            freq={}
            for vehicles in self.hubs.values():
                for v in vehicles:
                        freq[v.maintenance]=freq.get(v.maintenance, 0)+1
            return freq
    def display_Maintenance_status(self):
            freq = self.total_count_maintenance()
            print(f"<----Fleet Status Summary---->")
            total =0
            for v, m in freq.items():
                print(f"{v:<20}   :   {m}")
                total+= m
            print("-"*30)
            print(f"{'Total Vehicles':<20}   :   {total} ")

