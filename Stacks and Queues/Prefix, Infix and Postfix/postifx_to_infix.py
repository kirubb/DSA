def postfix_to_infix(expr):
    stack=[]

    for ch in expr:

        if ch.isalnum():
            stack.append(ch)

        else:
            right=stack.pop()
            left=stack.pop()
            stack.append(f"({left}{ch}{right})")
    return stack[-1]

print(postfix_to_infix("ab+cd-*"))
