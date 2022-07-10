
class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size} -kWh battery.")

    def get_range(self):

        if self.battery_size == 75:
            range_km = 260
        elif self.battery_size == 100:
            range_km = 300

        print(f"This car can go about {range_km} miles on a full charge!")
