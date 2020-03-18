import CCoffeeShopGame
import math

class CCustomer():
    def clamp(self, value, lower, upper):
        return lower if value < lower else upper if value > upper else value
    def NormalizePrice(self, param1):
        return param1 / 100 / 10
    def DecideReaction(self):
        _loc1 = 0
        _loc2 = 0
        _loc3 = 0
        _loc1 = self.AssessRecipeQuality(CCoffeeShopGame.GetRecipe())
        _loc2 = self.NormalizePrice(CCoffeeShopGame.GetPrice())
        _loc3 = _loc1 - _loc2 * CCoffeeShopGame.GetkSatisfiedWithEquity()
        return _loc3

    def OnConsumptionDone(self):
        _loc1 = 0
        _loc2 = ""
        _loc3 = 0
        _loc1 = self.DecideReaction()
        CCoffeeShopGame.AddReputation(_loc1)

    def AssessRecipeQuality(self, recipe):
        _loc2 = 0
        _loc3 = 0
        _loc4 = 0
        _loc5 = 0
        _loc2 = self.clamp(recipe["Coffee"] / CCoffeeShopGame.GetIdealRecipe()["Coffee"], 0, 1)
        _loc3 = self.clamp(recipe["Milk"] / CCoffeeShopGame.GetIdealRecipe()["Milk"], 0, 1)
        _loc4 = self.clamp(recipe["Sugar"] / CCoffeeShopGame.GetIdealRecipe()["Sugar"], 0, 1)
        _loc5 = _loc2 * _loc3 * _loc4
        return _loc5