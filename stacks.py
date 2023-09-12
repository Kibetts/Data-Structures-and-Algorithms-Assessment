def is_balanced(expression):
    stack = []
    opening = ['(','[','{']
    closing = [')',']','}'] 

    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if closing.index(char) != opening.index(stack.pop()):
                return False
    return not stack

expression1 = "([]{})"
expression2 = "([)]"

print(is_balanced(expression1)) # True
print(is_balanced(expression2)) # False