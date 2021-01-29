class MyInteger:
    def __init__(self, _value = 0): # _value : int, str, float, object
        checkType = type(_value)
        if (checkType == int) or (checkType == str) or (checkType == float) or (checkType == object):
            self.currValue = int(_value)
        else:
            self.currValue = 0

        self.count = 0 # 횟수
        self.record = [] # 기록

    def __equ__(self, other):
        checkType = type(other)
        if (checkType == int) or (checkType == str) or (checkType == float) or (checkType == object):
            if (self.currValue == int(other)):
                return True
            else:
                return False
        else:
            return False

    def pressAdd(self, _pressValue):
        _pressValue = int(_pressValue)
        self.currValue += _pressValue

        self.record.append(self.currValue)
        self.count += 1

        return self.currValue

    def pressSub(self, _pressValue):
        _pressValue = int(_pressValue)
        self.currValue -= _pressValue

        self.record.append(self.currValue)
        self.count += 1

        return self.currValue

    def getCurrentVariable(self, _mode = None):
        if (_mode is None):
            return self.currValue # 10진수 그대로
        else:
            if (_mode == 'hex'):
                self.changeMode = hex(self.currValue)
            elif (_mode == 'oct'):
                self.changeMode = oct(self.currValue)
            elif (_mode == 'bin'):
                self.changeMode = bin(self.currValue)
            return self.changeMode # 변환값

    def resetCurrentVariable(self):
        self.currValue = 0
        self.changeMode = 0

        self.record = []
        self.count = 0

        return self.currValue

    def rollbackCurrentVariable(self):
        # 직전에 수행한 값으로 복귀
        self.count -= 1
        if (self.count < 0):
            self.count = 0
        else:
            self.currValue = self.record.pop()
            self.count -= 1
        return self.currValue
            