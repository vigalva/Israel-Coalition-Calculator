class Coalition:
    def __init__(self,parties,value):
        self.parties=parties
        self.value=value

    def getValue(self):
        return self.value

    def getParties(self):
        return self.parties

    def __repr__(self):
            return "Coalition=" + str(self.getParties()) + "- value=" + str(self.getValue())


