import csv
from random import randrange

class Player:

    def __init__(self, _playerId = 'noname'):
        self.playerId = _playerId

    def getId(self):
        return self.playerId

    def setValue(self, _value = None):
        if (_value is not None):
            self.value = _value
        else:
            self.value = randrange(0,3)

    def getValue(self):
        return self.value

class Game:

    gameResult = []

    def __init__(self, _player1 = None, _player2 = None, _session = None):
        self.status = True
        if (_player1 is not None) and (_player2 is not None) and (_session is not None):
            self.player1 = _player1
            self.player2 = _player2
            self.session = _session
        else:
            self.status = False

    def runGame(self, _val1 = None, _val2 = None):
        if (self.status == True):
            if (_val1 is not None) and (_val2 is not None):
                self.val1 = _val1
                self.val2 = _val2
            else:
                self.val1 = randrange(0,3)
                self.val2 = randrange(0,3)
            return (self.val1, self.val2)
        else:
            return (-1,-1)

    def decideWinner(self):
        if (self.val1 == 0): # 가위
            if (self.val2 == 0): # 가위
                self.winner = 0
            elif (self.val2 == 1): # 바위
                self.winner = 2
            elif (self.val2 == 2): # 보
                self.winner = 1

        elif (self.val1 == 1): # 바위
            if (self.val2 == 0): # 가위
                self.winner = 1
            elif (self.val2 == 1): # 바위
                self.winner = 0
            elif (self.val2 == 2): # 보
                self.winner = 2

        elif (self.val1 == 2): # 보
            if (self.val2 == 0): # 가위
                self.winner = 2
            elif (self.val2 == 1): # 바위
                self.winner = 1
            elif (self.val2 == 2): # 보
                self.winner = 0
        
        return self.winner

    def logGame(self):
        if (self. status == True):
            row = str(self.session) + ',' + self.player1 + ',' + str(self.val1) + ',' + self.player2 + ',' + str(self.val2) + ',' + str(self.winner)
            Game.gameResult.append(row.split(','))
            #print(row.split(',')+'\n')
        return self.status
        
    def closeSession(self):
        if (self.status == True):
            head = "session,player1,choice1,player2,choice2,winner".split(',')
            Game.gameResult.insert(0,head) # 0번 idx에 row 내용을 삽입
            print(Game.gameResult) # for check
        
            with open("output.csv", 'w') as f:
                for line in Game.gameResult:
                    f.write(','.join(line)+'\n')

        return self.status

listValue = [0,1,2] # 0:가위, 1:바위, 2:보

# for check
# p1 = Player("김연수")
# p2 = Player("김민지")

# p1.setValue(2)
# p2.setValue(1)

# g1 = Game(p1.getId(), p2.getId(), 1)
# g1.runGame(p1.getValue(), p2.getValue())
# g1.decideWinner()
# g1.logGame()
# g1.closeSession()
