from abc import ABC
from vehicle_type import VehicleType

class Vehicle(ABC): #abstract class 
    def __init__(self, license_plate:str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.type=vehicle_type

    def get_type(self) -> VehicleType: #not an abstract method since we didn't use @abstractmethod decorator.
        return self.type