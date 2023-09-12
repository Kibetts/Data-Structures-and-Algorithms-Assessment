def is_balanced(expression):
    stack = []
    opening = set('([{') 
    closing = set(')]}')
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            if closing.index(char) != opening.index(stack.pop()):
                return False
    return not stack