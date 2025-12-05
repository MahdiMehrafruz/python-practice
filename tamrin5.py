class Vehicle :
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def display_info (self):
        print(f"brand name : {self.brand}")
        print(f"year : {self.year}")
        

class car (Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors
    
    def display_info(self):
        super().display_info()
        print(f"number of doors: {self.num_doors}")


class Motorcycle (Vehicle):
    def __init__(self, brand, year,sidecar):
        super().__init__(brand, year)
        self.sidecar = sidecar

    def display_info(self):
        super().display_info()
        if self.sidecar == True:
            print("sidecar : Yes")
        else:
            print("sidecar : No")

v1 = Vehicle("Kawasaki", 2010)
c1 = car("BMW",2017,4)
m1 = Motorcycle("Harley",2005,True)

        
v1.display_info ()
c1.display_info ()
m1.display_info ()




