print("""
---------------------------------------------------------------------
      WELCOME TO ECO-RIDE URBAN MOBILE SYSTEM
-----------------------------------------------------------------------""")
from abc import ABC, abstractmethod
from models.vehicle import Vehicle
from models.Electric_Cars import Electric_Cars
from models.Scooters import Scooters
from services.fleet_management import Fleet_Management
#__main__
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


# print("\nVehicles in Downtown Hub:")
# for v in fleet.search_by_hub("Downtown"):
#     print(v.vehicle_id, v.model, v.battery_percentage)




print("\nVehicles with Battery > 80%:")

high_battery = fleet.get_vehicle_battery()

for v in high_battery:
    print(v.vehicle_id, v.model, v.battery_percentage)

# __USE CASE 9___main
fleet.display_vehicle_type()


# USE CASE 10

car1.maintenance="Under Maintenance"
print(car1.maintenance)
print(fleet.total_count_maintenance())
fleet.display_Maintenance_status()

#USE CASE 11
# print(fleet.sort_hub_vehicle('Downtown'))
fleet.display_sorted_by_model('Downtown')

print(car1)
print(car2)
print(scooter1)
print(scooter2)