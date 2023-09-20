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
    operater_stack = []

    opening_parenthesis_counter = 0
    closing_parenthesis_counter = 0

    for token in tokenized_expression:
        if token.isdigit():
            output.append(token)
        elif token in operator_precedence.keys():
            while operater_stack and operator_precedence[token] <= operator_precedence[operater_stack[-1]] and operater_stack[-1] != '(':
                output.append(operater_stack.pop())
            operater_stack.append(token)
        elif token == '(':
            opening_parenthesis_counter += 1
            operater_stack.append(token)
        elif token == ')':
            closing_parenthesis_counter += 1
            while operater_stack and operater_stack[-1] != "(":
                output.append(operater_stack.pop())
            operater_stack.pop()
        else:
            continue

    while operater_stack:
        output.append(operater_stack.pop())

    if opening_parenthesis_counter != closing_parenthesis_counter:
        print("warning: parenthesis mismatch detected")

    return output


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
    expression = "1 + 1 - 3 * 12"
    tokenized_expression = tokenizer(expression, list(operator_to_precedence.keys()))
    rpn = shunting_yard(tokenized_expression, operator_to_precedence)
    print("Expression: " + expression)
    print("Tokenized Expression: " + str(tokenized_expression))
    print("RPN: " + str(rpn))
