class CRandom():
    _seed = 0
    def CRandom(self, num):
        self._seed = 0
        self.SetSeed(num)
    def SetSeed(self, seed):
        self._seed = seed
    def GetBoolean(self):
        return self.GetRandom() < 0.5
    def GetIntInRange(self, num, num2):
        return int(num + self.GetRandom() * (num2 - num + 1))
    def GetNumInRange(self, num, num2):
        return num + self.GetRandom() * (num2 - num + 1)
    def GetRandom(self):
        self._seed = (self._seed * 9301 + 49297) % 233280
        return self._seed / 233280
