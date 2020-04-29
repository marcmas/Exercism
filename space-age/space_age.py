class SpaceAge:
    def __init__(self, seconds: float):
        self.year = seconds / 31557600
        self.period = {"Mercury": 0.2408467, "Venus": 0.61519726, "Mars": 1.8808158, "Jupiter": 11.862615, "Saturn": 29.447498, "Uranus": 84.016846, "Neptune": 164.79132}

    def on_earth(self):
        return round(self.year, 2)

    def on_mercury(self):
        return round(self.year / self.period["Mercury"], 2)

    def on_venus(self):
        return round(self.year / self.period["Venus"], 2)

    def on_mars(self):
        return round(self.year / self.period["Mars"], 2)

    def on_jupiter(self):
        return round(self.year / self.period["Jupiter"], 2)

    def on_saturn(self):
        return round(self.year / self.period["Saturn"], 2)

    def on_uranus(self):
        return round(self.year / self.period["Uranus"], 2)

    def on_neptune(self):
        return round(self.year / self.period["Neptune"], 2)