
class Weather:
    def __init__(self, location:str, temperature:int, snow:float, rain:float,wind:int, ranking=None):
        self.location=location
        self.rain=rain
        self.snow=snow
        self.wind=wind
        self.temperature=temperature
        return

    