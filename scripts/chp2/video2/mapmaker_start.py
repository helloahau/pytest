class Point():
    def __init__(self, city, latitude, longitude):
        self._city = city
        self._latitude = latitude
        self.longitude = longitude

    def get_lat_long(self):
        return (self._latitude, self.longitude)
