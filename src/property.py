"""## Property

Property type in class"""

from typing import Optional


class Human:
    """Human class

    Attributes:
        heigh (float): height in meter

    Examples:
        Getting high in different scalar

        >>> human = Human(1.75) # in meters
        >>> human.get_height("inch")
        68.897675
    """

    def __init__(self, height: float) -> None:
        self.height = height

    def get_height(self, unit: Optional[str] = None) -> float:
        """Getting heigh of human

        Args:
            unit (Optional[str]): dessirable scalar,
                if None then it will return the main heigh in meters

        Returns:
            float: height with respectable scalar
        """
        mapper = {"inch": 39.3701, "foot": 3.28084}
        if unit:
            if unit in mapper.keys():
                return self.height * mapper[unit]
            raise KeyError("Not found 'unit'")
        return self.height

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if value > 1.628:
            self.desc = "above average"
        elif value == 1.628:
            self.desc = "average"
        else:
            self.desc = "below average"
        self._height = value
