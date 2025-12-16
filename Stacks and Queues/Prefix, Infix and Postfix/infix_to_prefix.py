def infix_to_prefix(expr):
    # reverse expression and swap brackets
    expr = expr[::-1]
    expr = expr.replace('(', '#').replace(')', '(').replace('#', ')')

    stack = []
    postfix = []

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
            stack.pop()

        # operator
        else:
            while stack and stack[-1] != '(':
                top = stack[-1]

                # NOTE: here ^ is treated as LEFT associative
                if prec[top] > prec[ch] or prec[top] == prec[ch]:
                    postfix.append(stack.pop())
                else:
                    break

            stack.append(ch)

    while stack:
        postfix.append(stack.pop())

    # reverse postfix to get prefix
    return ''.join(postfix[::-1])


# Example
print(infix_to_prefix("a+b-*(c^d^e-f)"))
print(infix_to_prefix("(a+b)*c-d+e"))
