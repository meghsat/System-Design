from parking_lot import ParkingLot
from level import Level
from motorcycle import Motorcycle

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 100))
        parking_lot.add_level(Level(2, 80))

        motorcycle = Motorcycle("M1234")

        parking_lot.park_vehicle(motorcycle)

        parking_lot.display_availability()

        parking_lot.unpark_vehicle(motorcycle)

        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()