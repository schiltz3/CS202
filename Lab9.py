from math import pi, sqrt

# John Schiltz


class Cone:
    """Class that represents a cone and provides useful methods to calculate metrics about the cone"""

    def __init__(self, radius: float, height: float, weight: float):
        """Create a cone with the given radius, height and weight

        Args:
            radius (float): the radius of the cone
            height (float): The height of the cone
            weight (float): The weight of the cone
        """
        self.radius = radius
        self.height = height
        self.weight = weight

    def volume(self) -> float:
        """Get the volume of the cone

        Returns:
            float: The volume of the cone
        """
        return 1 / 3 * (pi * (self.radius**2)) * self.height

    def getWeight(self) -> float:
        """Get the weight of the cone

        Returns:
            float: The weight of the cone
        """
        return self.weight

    def density(self) -> float:
        """get the density of the cone

        Returns:
            float: the density of the cone
        """
        return self.getWeight() / self.volume()

    def slantHeight(self) -> float:
        """Get the slant height of the cone

        Returns:
            float: The slant height of the cone
        """
        return sqrt((self.radius**2) + (self.height**2))


print(help(Cone))
print(help(Cone.volume))
print("\nCone 1")
cone1 = Cone(4, 2, 10)
print(f"Density: {cone1.density()}")
print(f"Volume: {cone1.volume()}")
print(f"Weight: {cone1.getWeight()}")
print("\nCone2")
cone2 = Cone(1, 1, 1)
print(f"Slant height: {cone2.slantHeight()}")
print("\nCone3")
cone3 = Cone(0, 0, 0)
print(f"Volume: {cone3.volume()}")
