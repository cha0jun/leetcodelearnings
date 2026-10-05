'''
Given a string containing only ()[]{}, return whether it's valid: every opener is closed by the same type, in the correct order.
'''

def is_valid(input:str) -> bool:
    # maintain a stack, append if left, pop if right, if correct order, stack should be empty by end
    stack = []
    pairs = {")" : "(", "]": "[", "}": "{"}
    for i in input:
        if i in "({[":
            # append opener
            stack.append(i)
        elif stack and stack[-1] == pairs[i]:
            # last item in stack correct opener for this closing bracket
            stack.pop()
        else:
            return False # not a bracket
    
    return not stack

assert is_valid("()[]{}") == True
assert is_valid("(]") == False
assert is_valid("([)]") == False
assert is_valid("{[]}") == True
