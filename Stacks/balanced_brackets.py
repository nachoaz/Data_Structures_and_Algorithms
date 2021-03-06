# balanced_brackets.py
"""
https://www.hackerrank.com/challenges/balanced-brackets
"""


from stack import Stack


def is_balanced(s):
    if len(s) % 2 == 1:
        return 'NO'
    else:
        stack = Stack()
        counterparts = {'{':'}', '[':']', '(':')'}
        
        for char in s:
            if char in counterparts:
                stack.push(char)
            elif stack.is_empty() or counterparts[stack.pop()] != char:
                return 'NO'
                    
        return 'YES' if stack.is_empty() else 'NO'
        

def main():
    n = int(input())

    for _ in range(n):
        bracket_string = input()
        output = is_balanced(bracket_string)
        print(output)


if __name__ == '__main__':
    main()
