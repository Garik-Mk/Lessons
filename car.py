


class Car():
    def __init__(self,
                name: str,
                year: int,
                sign: str,
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
        # # # # # # # # # #
        # YOUR CODE HERE! #
        # # # # # # # # # #


    def calculate_time(self, distance: float) -> float:
        """Calculate time needed to travel distance.

        Parameters:
        -----------
            distance (float):           [Distance wished to travel]

        Returns:
        --------
            float:                      [Time needed to travel that distance]
        """
        # # # # # # # # # #
        # YOUR CODE HERE! #
        # # # # # # # # # #


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
        # # # # # # # # # #
        # YOUR CODE HERE! #
        # # # # # # # # # #


    def fill(self, fuel_amount: float) -> None:
        """Fill car tank with the amount specified.

        Fill car tank, but do not exceed the tank's capacity.


        Parameters:
        ----------
            fuel_amount (float):        [Amount needed to be filled]
        """
        # # # # # # # # # #
        # YOUR CODE HERE! #
        # # # # # # # # # #


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
        # # # # # # # # # #
        # YOUR CODE HERE! #
        # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # GETTERS # # # # # # # # # # # # # # # # # #

    def get_sign(self) -> str:
        """Return car registration sign."""
        # # # # # # # # # #
        # YOUR CODE HERE! #
        # # # # # # # # # #


    def get_fuel(self) -> float:
        """Return left fuel amount."""
        # # # # # # # # # #
        # YOUR CODE HERE! #
        # # # # # # # # # #


    def max_distance_can_travel(self) -> float:
        """Return max distance car can travel with current fuel amount"""
        # # # # # # # # # #
        # YOUR CODE HERE! #
        # # # # # # # # # #




# Write an example for usage of your Car class.
# # # # # # # # # #
# YOUR CODE HERE! #
# # # # # # # # # #
