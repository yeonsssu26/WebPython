import csv

class RemoteControl:
    def __init__(self):
        self.__enabledChannelList = [] # 채널관리
        self.favor = [] # 선호도관리
        self.currChannelIdx = 0
        self.status = True

    def powerOnRemoteControl(self, _channel): #_channel : [채널번호, 채널이름]
        self.__enabledChannelList.append(_channel)
        self.countChannel = len(self.__enabledChannelList)

        self.favor.append([_channel[0],0]) # [채널번호, 선호도]

        #print(self.__enabledChannelList) # for check
        #print(self.favor) # for check

        return self.countChannel

    def gotoChannel(self, _gotoNumber):
        for i in range(len(self.__enabledChannelList)):
            if(self.__enabledChannelList[i][0] == _gotoNumber):
                if ((self.__enabledChannelList[i][1] == self.blockChannel()) and (self.status == False)):
                    print("channel is blocked : error at gotoChannel")
                else:
                    self.currChannelIdx = i
                    return self.__enabledChannelList[i][1] # 바뀐 채널 이름 return
        return self.__enabledChannelList[self.currChannelIdx][1] # 원래 보던 채널 이름 return

    def nextChannel(self):
        if (self.currChannelIdx == len(self.__enabledChannelList)-1):
            self.back = 0
        else:
            self.back = self.currChannelIdx + 1

        if (self.__enabledChannelList[self.back][1] == self.blockChannel() and self.status == False):
            print("channel is blocked : error at nextChannel")
        else:
            self.currChannelIdx = self.back
            self.currChannelName = self.__enabledChannelList[self.currChannelIdx][1]
            return self.currChannelName

    def previousChannel(self):
        if (self.currChannelIdx == 0):
            self.front = len(self.__enabledChannelList)-1
        else:
            self.front = self.currChannelIdx - 1

        if (self.__enabledChannelList[self.front][1] == self.blockChannel() and self.status == False):
            print("channel is blocked : error at previousChannel")
        else:
            self.currChannelIdx = self.front
            self.currChannelName = self.__enabledChannelList[self.currChannelIdx][1]
            return self.currChannelName

    def blockChannel(self):
        self.status = False # False : block
        self.block = self.currChannelIdx
        
        if (self.currChannelIdx == len(self.__enabledChannelList)-1):
            self.back = 0
        else:
            self.back = self.currChannelIdx + 1

        self.currChannelName = self.__enabledChannelList[self.currChannelIdx][1]
        return self.currChannelName

    def unblockChannel(self, _blockToUnblock):
        if (_blockToUnblock == self.__enabledChannelList[self.block][0]):
            self.status = True # True : unblock
            self.block = 0
            return 1
        else:
            return -1 

    def powerOffRemoteControl(self):
        f = open("output.csv",'w')
        for i in range(len(self.__enabledChannelList)):
            row = []
            for j in range(len(self.__enabledChannelList[i])):
                if (j == 0):
                   row.append(str(self.__enabledChannelList[i][j]))
                elif (j == 1):
                    row.append(self.__enabledChannelList[i][j])
            #print(row)
            f.write(','.join(row)+'\n')
        f.close()

    def favorChannel(self):
        if(self.__enabledChannelList[self.currChannelIdx][1] == self.blockChannel() and self.status == False):
            return -1
        else:
            self.favor[self.currChannelIdx][1] = self.favor[self.currChannelIdx][1] + 1
            return 1

    def aiNextChannel(self):
        self.currFavor = self.__enabledChannelList[self.currChannelIdx][1]
        self.sortFavorReverse = sorted(self.__enabledChannelList, key = lambda x : x[1], reverse=True)
        for i in range(len(self.sortFavorReverse)):
            if (self.currFavor > self.sortFavorReverse[i][1]):
                if(self.sortFavorReverse[i][1] == self.blockChannel() and self.status == False):
                    continue
                self.lessFavor = self.sortFavorReverse[i][1]
                return self.lessFavor
        self.lessFavor = self.sortFavorReverse[0][1]
        return self.lessFavor

    def aiPreviousChannel(self):
        self.currFavor = self.__enabledChannelList[self.currChannelIdx][1]
        self.sortFavor = sorted(self.__enabledChannelList, key = lambda x : x[1])
        for i in range(len(self.sortFavor)):
            if (self.currFavor < self.sortFavor[i][1]):
                if(self.sortFavor[i][1] == self.blockChannel() and self.status == False):
                    continue
                self.moreFavor = self.sortFavor[i][1]
                return self.moreFavor
        self.moreFavor = self.sortFavor[-1][1]
        return self.moreFavor

# for check
# c1 = RemoteControl()

# c1.powerOnRemoteControl([6,'SBS'])
# c1.powerOnRemoteControl([7,'KBS'])
# c1.powerOnRemoteControl([9,'KBS1'])
# c1.powerOnRemoteControl([11,'MBC'])

# print(c1.gotoChannel(9))
# print(c1.nextChannel())
# print(c1.previousChannel())

# print(c1.blockChannel())
# print(c1.unblockChannel(7))
# print(c1.unblockChannel(9))

# c1.powerOffRemoteControl()

# c1.favorChannel()
# c1.favorChannel()

# print(c1.gotoChannel(6))
# c1.favorChannel()
# print(c1.nextChannel())
# c1.favorChannel()
# c1.favorChannel()
# c1.favorChannel()
# c1.favorChannel()
# c1.favorChannel()
# print(c1.previousChannel())

# print(c1.aiNextChannel())
# print(c1.aiPreviousChannel)
