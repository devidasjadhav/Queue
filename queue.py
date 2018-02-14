#!/usr/bin/python
stk1 = []
stk2 = []

def enque(item):
  if stk2:
    while len(stk2) > 0 : stk1.append(stk2.pop())
  stk1.append(item)

def deque():
  if stk1:
    while len(stk1) > 0 : stk2.append(stk1.pop())
  return stk2.pop()

###############################################################################################################
###########################################   TEST QUEUE ######################################################
###############################################################################################################

print stk1
print stk2
print enque(1)

print stk1
print stk2
print enque(2)

print stk1
print stk2
print enque(3)

print stk1
print stk2
print enque(4)

print stk1
print stk2
print deque()

print stk1
print stk2
print deque()

print stk1
print stk2
print deque()

print stk1
print stk2
print deque()
