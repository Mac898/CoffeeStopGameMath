class CCoffeeShopGame():
    def __init__(self):
        self.recipe = {
        "Coffee": 2,
        "Milk": 1,
        "Sugar": 2,            
        }
        self.kSatisfiedWithEquity = 1
        self.sellPrice = 2
        self.temperature = 51
        self.IdealRecipe = {
        "Coffee": 4,
        "Milk": 2,
        "Sugar": 4,
        }
    def GetRecipe(self):
        return self.sellPrice
    def GetkSatisfiedWithEquity(self):
        return self.kSatisfiedWithEquity
    def GetMinTemperature(self):
        return 20
    def GetMaxTemperature(self):
        return 80
    def GetTemperature(self):
        return self.temperature
    def GetPrice(self):
        return self.sellPrice