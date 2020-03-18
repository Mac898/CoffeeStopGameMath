import CCoffeeShopGame

class CCustomer():
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

    