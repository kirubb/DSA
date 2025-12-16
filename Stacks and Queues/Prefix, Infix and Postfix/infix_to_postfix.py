def infix_to_postfix(expr):
    stack = []
    postfix = []

    # precedence
    prec = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    for ch in expr:
        # operand
        if ch.isalnum():
            postfix.append(ch)

        # opening bracket
        elif ch == '(':
            stack.append(ch)

        # closing bracket
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()   # remove '('

        # operator
        else:
            while stack and stack[-1] != '(':
                top = stack[-1]

                # higher precedence
                if prec[top] > prec[ch]:
                    postfix.append(stack.pop())

                # same precedence & left associative
                elif prec[top] == prec[ch] and ch != '^':
                    postfix.append(stack.pop())

                else:
                    break

            stack.append(ch)

    # pop remaining operators
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


# Example
print(infix_to_postfix("a^b^c"))
print(infix_to_postfix("(a+b)*c"))
print(infix_to_postfix("a+b*c"))
