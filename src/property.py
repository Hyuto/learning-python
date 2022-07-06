class Human:
    """Human class

    Args:
        heigh (float): height in meter
    """

    def __init__(self, height: float):
        self.height = height

    def get_height(self, unit=None):
        mapper = {"inch": 39.3701, "foot": 3.28084}
        if unit:
            if unit in mapper.keys():
                return self.height * mapper[unit]
            raise KeyError("Not found 'unit'")
        return self.height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 1.628:
            self.desc = "above average"
        elif value == 1.628:
            self.desc = "average"
        else:
            self.desc = "below average"
        self._height = value
