#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    stack = []
    
    for char in brackets:
        if char in '({[':
            stack.append(char)
  
        if char in '})]':
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return 'NO'
    
    if len(brackets) == 0:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
