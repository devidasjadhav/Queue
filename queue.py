#!/usr/bin/python
stk1 = []
stk2 = []

def enque(item):
    if not stk1:
        stk2.append(item)
    else:
        while len(stk2) > 1 : stk1.append(stk2.pop())
    stk1.append(item)

def deque():
    if not stk2:
        if not stk1:
            print "Error Empty Queue"
            return "Error"
        else:
            while len(stk1) > 2:
                stk2.append(stk1.pop())
            ret = stk1.pop()
            stk1.pop()
            return ret
    else:
        return stk2.pop()


print stk1
print stk2
print enque(1)


print stk1
print stk2
print enque(4)


print stk1
print stk2
print deque()

print stk1
print stk2
print enque(2)

print stk1
print stk2
print enque(3)

print stk1
print stk2
print deque()

print stk1
print stk2
print deque()

print stk1
print stk2
print deque()
