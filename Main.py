def tokenizer(user_input: str, operator_list: list) -> list:
    token_builder = ""
    tokenized_list = []
    for char in user_input:
        if char.isdigit():
            token_builder += char
        elif char in operator_list:
            tokenized_list.append(token_builder)
            tokenized_list.append(char)
            token_builder = ""
        else:
            continue
    tokenized_list.append(token_builder)
    return tokenized_list


def shunting_yard(tokenized_expression: list, operator_precedence: dict):
    output = []
    operator_stack = []

    opening_parenthesis_counter = 0
    closing_parenthesis_counter = 0

    for token in tokenized_expression:
        if token.isdigit():
            output.append(token)
        elif token in operator_precedence.keys():
            while operator_stack and operator_precedence[token] <= operator_precedence[operator_stack[-1]] and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            opening_parenthesis_counter += 1
            operator_stack.append(token)
        elif token == ')':
            closing_parenthesis_counter += 1
            while operator_stack and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            operator_stack.pop()
        else:
            continue

    while operator_stack:
        output.append(operator_stack.pop())

    if opening_parenthesis_counter != closing_parenthesis_counter:
        print("warning: parenthesis mismatch detected")

    return output


# TODO: This function gives a 'list index out of range' error if a number token consists of more than one digit. fix it
def rpn_evaluate(expression: list):
    for token in expression[:]:
        if not token.isdigit():
            token_index = expression.index(token)

            if token == '+':
                expression[token_index-2] = float(expression[token_index-2]) + float(expression[token_index-1])
            if token == '-':
                expression[token_index - 2] = float(expression[token_index - 2]) - float(expression[token_index - 1])
            if token == '*':
                expression[token_index - 2] = float(expression[token_index - 2]) * float(expression[token_index - 1])
            if token == '/':
                expression[token_index - 2] = float(expression[token_index - 2]) / float(expression[token_index - 1])
            if token == '^':
                expression[token_index - 2] = float(expression[token_index - 2]) ** float(expression[token_index - 1])

            expression.pop(token_index)
            expression.pop(token_index-1)

    return expression[0]



if __name__ == "__main__":
    operator_to_precedence = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
        '^': 2,
        '(': 3,
        ')': 3
    }

    # Tests
    expression = input("Please enter an expression to evaluate: ")
    tokenized_expression = tokenizer(expression, list(operator_to_precedence.keys()))
    rpn = shunting_yard(tokenized_expression, operator_to_precedence)
    result = rpn_evaluate(rpn)
    print("Expression: " + expression)
    print("Tokenized Expression: " + str(tokenized_expression))
    print("RPN: " + str(rpn))
    print("result: " + str(result))
