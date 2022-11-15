from collections import deque

word = 'raceca1r'

def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False
    return True


print(palindrome(word))


print(word[::-1])

