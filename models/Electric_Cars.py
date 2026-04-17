from models.vehicle import Vehicle
class Electric_Cars(Vehicle):
        def __init__(self, vehicle_id, model, battery_percentage,seating_capacity):
                super().__init__(vehicle_id, model, battery_percentage)
                self.seating_capacity=seating_capacity
        def calculate_trip_cost(self, distance):
                self.distance=distance
                total = 5 + 0.5*(self.distance)
                return f"Total trip coast :{total:.2f}"
