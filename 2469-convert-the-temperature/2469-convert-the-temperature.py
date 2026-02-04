class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        kelvin = celsius + 273.15
        Fahrenheit = celsius*9/5 + 32

        return [kelvin, Fahrenheit]