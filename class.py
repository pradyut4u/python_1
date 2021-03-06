class Basketball():
    def __init__(self,team,playerno,gamesplayed,gameswon):
        self.team=team
        self.playerno=playerno
        self.gamesplayed=gamesplayed
        self.gameswon=gameswon
    def gameslost(self):
        print(self.gamesplayed - self.gameswon)
mavericks=Basketball('mavericks',5,8,6)
jordan=Basketball('jordan',4,7,4)
mavericks.gameslost()
print(mavericks.playerno)
print(jordan.team)