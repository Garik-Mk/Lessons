


class Car():
    def __init__(self,
                name: str,
                year: int,
                speed: float,
                consumption: float,
                tank_size: float
                ) -> None:
        """
        Fields:
        -------
            Public:
                name (str):             [Name of vehicle]
                year (int):             [Year of production]
                speed (float):          [Vehicle average speed]
                consumption (float):    [Fuel consumption on 100 km (litres)]
                tank_size (float):      [Vehicle tank size (litres)]
            Private:
                __fuel__ (float):       [Current fuel amount]
                __sign__ (str):         [Registration Sign]
        """
        self.name = name
        self.year = year
        self.speed =speed 
        self.consumption = consumption
        self.tank_size = tank_size

        self.__fuel__ = 0
        # if len(sign) != 7:
        #     self.__sign__ = ''
       
        # elif sign[:2].isdigit() and sign[2:4].isalpha() and\
        #         sign[2:4].isupper() and sign[4:8].isdigit():
        #     self.__sign__ = sign


    def calculate_time(self, distance: float) -> float:
        """Calculate time needed to travel distance.

        Parameters:
        -----------
            distance (float):           [Distance wished to travel]

        Returns:
        --------
            float:                      [Time needed to travel that distance]
        """
        
        return distance / self.speed


    def register(self, new_sign_number: str) -> bool:
        """Check if new sign is valid and register it if yes.

        Validation means, the first two chars of new sign must be digits,
        followed by two uppercase letters and 3 digits.
        Also, if car is already registered, return False and do not
        change anything.

        Parameters:
        -----------
            new_sign_number (str):      [New sign number]

        Returns:
        --------
            bool:                       [Registered or not]
        """
        
        if len(new_sign_number) != 7:
            return False

        if new_sign_number == self.__sign__:
            return False
        
        elif new_sign_number[:2].isdigit() and new_sign_number[2:4].isalpha() and\
                new_sign_number[2:4].isupper() and new_sign_number[4:8].isdigit():
            self.__sign__ = new_sign_number
            return True
        else:
            return False


    def fill(self, fuel_amount: float) -> None:
        """Fill car tank with the amount specified.

        Fill car tank, but do not exceed the tank's capacity.


        Parameters:
        ----------
            fuel_amount (float):        [Amount needed to be filled]
        """
        
        self.__fuel__ = min(self.__fuel__ + fuel_amount, self.tank_size)
        return 


    def go(self, distance: float) -> bool:
        """Travel providen distance

        Calculate the fuel amount needed to be spent on the distance.
        If there is enough fuel, calculate how much fuel is left after distance,
        write the result in car's fuel amount field and return True.
        If there isn't enough fuel, return False.

        Parameters:
        -----------
            distance (float):           [Distance wished to travel]

        Returns:
        --------
            bool:                      [Traveled or not]
        """
        
        fuel_needed = distance / 100 * self.consumption
        if fuel_needed <= self.__fuel__:
            self.__fuel__ -= fuel_needed
            return True
        return False
    # # # # # # # # # # # # # # # # # # GETTERS # # # # # # # # # # # # # # # # # #

    def get_sign(self) -> str:
        """Return car registration sign."""
        
        return self.__sign__


    def get_fuel(self) -> float:
        """Return left fuel amount."""
        
        return self.__fuel__


    def max_distance_can_travel(self) -> float:
        """Return max distance car can travel with current fuel amount"""
    
        return self.__fuel__ / self.consumption * 100




# Write an example for usage of your Car class.

audi = Car('R8', 2020, '45AA654', 320, 25, 50)

print(audi.get_fuel())
audi.fill(80)
print(audi.get_fuel())
print(audi.get_sign())
audi.register('45aA999')
print(audi.get_sign())
audi.register('45AA999')
print(audi.get_sign())
print(str(audi.calculate_time(1200)) + ' hours')
print(audi.go(500))
print(audi.max_distance_can_travel())
print(audi.go(200))
print(audi.go(5))
print(audi.get_fuel())
audi.fill(20)
print(audi.go(5))
