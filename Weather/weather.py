
class Weather:
    def __init__(self, location:str, temperature:int, snow:int, rain:int,wind:int):
        self.location=location
        self.rain=rain
        self.snow=snow
        self.wind=wind
        self.temperature=temperature
        return