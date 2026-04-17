from models.vehicle import Vehicle

class Scooters(Vehicle):
      def __init__(self, vehicle_id, model, battery_percentage,max_speed_limit):
            super().__init__(vehicle_id, model, battery_percentage)
            self.max_speed_limit=max_speed_limit
      def calculate_trip_cost(self, time):
            self.time=time
            total = 1 + 0.15*(self.time)
            return f"Total trip coast :{total:.2f}"
