from CCoffeeShopGame import CCoffeeShopGame
from CRandom import CRandom
import math


class CCustomer():
    def __init(self, game):
        self.game = game
        self.random = CRandom()
    def clamp(self, value, lower, upper):
        return lower if value < lower else upper if value > upper else value
    def NormalizePrice(self, param1):
        return param1 / 100 / 10
    def DecideReaction(self):
        _loc1 = 0
        _loc2 = 0
        _loc3 = 0
        _loc1 = self.AssessRecipeQuality(self.game.GetRecipe())
        _loc2 = self.NormalizePrice(self.game.GetPrice())
        _loc3 = _loc1 - _loc2 * self.game.GetkSatisfiedWithEquity()
        return _loc3

    def OnConsumptionDone(self):
        _loc1 = 0
        _loc2 = ""
        _loc3 = 0
        _loc1 = self.DecideReaction()
        self.game.AddReputation(_loc1)

    def AssessRecipeQuality(self, recipe):
        _loc2 = 0
        _loc3 = 0
        _loc4 = 0
        _loc5 = 0
        _loc2 = self.clamp(recipe["Coffee"] / self.game.GetIdealRecipe()["Coffee"], 0, 1)
        _loc3 = self.clamp(recipe["Milk"] / self.game.GetIdealRecipe()["Milk"], 0, 1)
        _loc4 = self.clamp(recipe["Sugar"] / self.game.gameShopGame.GetIdealRecipe()["Sugar"], 0, 1)
        _loc5 = _loc2 * _loc3 * _loc4
        return _loc5
    def GetDemand(self):
        _loc1 = 0
        _loc2 = 0
        _loc3 = 0
        _loc4 = 0
        _loc5 = 0
        _loc1 = 1 - 0.75 * (self.game.GetTemperature() - self.game.GetMinTemperature()) / (self.game.GetMaxTemperature - self.game.GetMinTemperature)
        _loc2 = 1 - self.game.GetPrice() / 100 / (10 / 0.9)
        _loc3 = self.game.GetReputation()
        _loc4 = 0.4
        _loc5 = _loc1 * _loc2 + _loc3 * _loc4
        return _loc5
    def DecideWantToPurchase(self):
        _loc1 = 0
        _loc2 = False
        _loc3 = ""
        _loc1 = self.GetDemand()
        _loc2 = self.random.GetRandom() < _loc1
        _loc3 = self.GetDominantReasonForDemand(_loc2)
        return _loc2
    def GetDominantReasonForDemand(self, bool1):
        _loc2 = []
        _loc3 = 0
        _loc4 = 0
        _loc5 = 0
        _loc6 = 0
        _loc7 = 0
        _loc3 = 1 - 0.75 * (self.game.GetTemperature() - self.game.GetMinTemperature()) / (self.game.GetMaxTemperature - self.game.GetMinTemperature)
        _loc4 = 1 - self.game.GetPrice() / 100 / (10 / 0.9)
        _loc5 = self.game.GetReputation()
        _loc6 = 0.5
        _loc2[0] = {
            "_weight":_loc3,
            "_reason":"Weather"
        }
        _loc2[1] = {
            "_weight":_loc4,
            "_reason":"Price"
        }
        _loc2[2] = {
            "_weight":abs(_loc5 * _loc6),
            "_reason":"Reputation"
        }
        if not(bool1):
            _loc2[0]["_weight"] = 1 - _loc2[0]["_weight"]
            _loc2[1]["_weight"] = 1 - _loc2[1]["_weight"]
            if _loc5 > 0:
               _loc2[2]["_weight"] = 0
        elif _loc5 < 0:
            _loc2[2]["_weight"] = 0
        _loc7_ = self.game.PickFromWeightedArray(_loc2)
        return _loc2[_loc7_]["_reason"]
    def OnConsideringDone(self):
        if self.DecideWantToPurchase():
            print("Customer Purchased")
