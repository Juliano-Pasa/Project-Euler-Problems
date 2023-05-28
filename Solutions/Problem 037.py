# https://projecteuler.net/problem=17


import math

class State:
    def __init__(self, value, totalDelimiters):
        self.value = value
        self.totalDelimiters = totalDelimiters
        self.expandable = False

    def ExpandNextStates(self):
        nextValue = self.value * 10

        state1 = State(nextValue + 1, self.totalDelimiters + 1) 
        state3 = State(nextValue + 3, self.totalDelimiters)
        state7 = State(nextValue + 7, self.totalDelimiters + 1)
        state9 = State(nextValue + 9, self.totalDelimiters)

        return [state1, state3, state7, state9]

    def CheckPrimality(self):
        self.expandable = False
        if self.totalDelimiters > 2:
            return False

        lastState = self.value % 10
        
        if self.totalDelimiters == 2:
            if lastState == 9:
                return False

        if not self.IsPrime(self.value):
            return False

        self.expandable = True

        if lastState == 1 or lastState == 9:
            return False

        aux = str(self.value)[1:]

        while len(aux) > 1:
            if not self.IsPrime(int(aux)):
                return False
            aux = aux[1:]

        return True
        
         
    def IsPrime(self, value):
        limit = math.sqrt(value)
        divisor = 3

        if value % 2 == 0 or value % 3 == 0 and value > 3:
            return False

        while divisor < limit:
            if value % divisor == 0:
                return False
            
            divisor += 2
        
        return True

if __name__ == "__main__":
    states = [State(3, 0), State(7, 1)]
    result = [23, 53]

    while len(states) > 0:
        current = states.pop(0)

        if current.CheckPrimality():
            result.append(current.value)

        if current.expandable:
            states.extend(current.ExpandNextStates())

    print(result)
    print(sum(result))