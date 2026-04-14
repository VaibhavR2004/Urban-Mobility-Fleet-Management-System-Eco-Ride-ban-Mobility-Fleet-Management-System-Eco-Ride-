class Vehicle:

    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id=vehicle_id
        self.model=model
        self.battery_percentage= battery_percentage

class Vehicle_data(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,maintenance_status, rental_price):
        super().__init__(vehicle_id, model, battery_percentage)
        self.__maintenance_status=maintenance_status
        self.__rental_price=rental_price

    @property
    def getter_maintenance(self):
        return f"{self.vehicle_id} maintenance is {self.__maintenance_status}"

    @property
    def getter_rental(self):
        return f"{self.vehicle_id} rental price {self.__rental_price}"

    def getter_batter(self):
        return f"{self.vehicle_id} battery is {self.battery_percentage}%"

    def setter_battery(self,battery_percentage):
        self.battery_percentage=battery_percentage if self.battery_percentage<=100 or self.battery_percentage>=0 else None

