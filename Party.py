from Position import  Position


class Party:

    def __init__(self,name,score,position):
        self.name=name
        self.score=score
        self.position=position

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def __repr__(self):
        return "Name=" + str(self.getName()) + ", Score=" + str(self.getScore())

    def __str__(self):
        return "Name=" + str(self.getName()) + ", Score=" + str(self.getScore())




