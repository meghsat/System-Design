from level import Level
from typing import List
from vehicle import Vehicle

class ParkingLot:
    _instance=None #class variable since it is defined outside any instance methods and directly attached
                   #to the class itself. Holds the single instance of the ParkingLot class[Singleton pattern: 
                   # acts as a storage location for the only object (or instance) of the ParkingLot class 
                   # that will exist during the application's runtime.]. Initially, assigned to None, 
                   # indicating no instance has been created yet.
    def __init__(self): #prevents multiple objects from being created. Any attempt to call ParkingLot() 
        if ParkingLot._instance is not None: #directly after the first creation will raise an exception.
            raise Exception("This is a Singleton class and there already exists an instance of this class")
        else:
            ParkingLot._instance = self #assigning the current object to _instance.
            self.levels:List[Level]=[] #levels is a list of type level
    
    @staticmethod #made static because it needs to be called without an instance of the class. This is crucial
    def get_instance(): # for implementing the Singleton pattern, as the whole point is to ensure there's 
                        #a way to get the single instance of the class before any instance exists.
        if ParkingLot._instance is None: #When an instance is requested, check if one has already been created
            ParkingLot()                 #or not. If not, create one and return the instance.
            return ParkingLot._instance                            

    def add_level(self, level: Level):
        self.levels.append(level)
    
    def park_vehicle(self, vehicle:Vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
    
    def display_availability(self) -> None:
        for level in self.levels:
            level.display_availability()