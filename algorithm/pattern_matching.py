import random, time, sys

scan = -1

ch = [' ', 'A', ' ', 'B', ' ', ' ', 'A', 'C', 'D', ' ']
next1 = [5,2,3,4,8,6,7,8,9,0]
next2 = [5,2,1,4,8,2,7,8,9,0]

class Deque:
    def __init__(self, size):
        self.deque = []
        self.first = int(size/2)
        self.last = int(size/2)

        for i in range(size):
            self.deque.append(0)

    def insertFirst(self, v):
        self.deque[self.first] = v
        self.first -= 1

    def insertLast(self, v):
        self.last += 1
        self.deque[self.last] = v

    def deleteFirst(self):
        self.deque[self.first] = 0
        self.first += 1
        return self.deque[self.first]

    def isEmpty(self):
        if (self.first == self.last):
            return True
        else:
            return False

    def checkDq(self):
        if (self.deque[self.first] == 0):
            if ((self.last - self.first < 2) and (self.deque[self.last] == scan)):
                return False
            elif (not self.isEmpty()):
                return True
            else:
                return False


    def prDq(self, size):
        for i in range(size):
            if(self.deque[i]==0):
                continue
            print(self.deque[i], end=' ')
        print()

def match(t):
    dq = Deque(100)
    j = 0
    N = len(t) -1
    state = next1[0]
    dq.insertLast(scan)
    
    while (state):
        dq.prDq(100)
        if (state == scan):
            j += 1
            if (dq.isEmpty()):
                dq.insertFirst(next1[0])
            dq.insertLast(scan)
        elif (ch[state] == t[j]):
            dq.insertLast(next1[state])
        elif (ch[state] == ' '):
            n1 = next1[state]
            n2 = next2[state]
            dq.insertFirst(n1)
            if (n1 != n2):
                dq.insertFirst(n2)
        if (dq.isEmpty()):
            return j
        if (j > N):
            return 0
        state = dq.deleteFirst()
        if (dq.checkDq()):
            state = dq.deleteFirst()

    return j-1


text = 'CDAABCAAABDDACDAACAAAAAAABD' + '\0'
previous = 0
i = 0
N = len(text) -1
while(True):
    pos = match(text[i:])
    if (pos <= 0):
        break
    pos += previous
    i = pos

    if (i <= N) :
        print('패턴이 나타난 위치 : ', pos)
    else:
        break
    previous = i
print('패턴 매칭 종료')