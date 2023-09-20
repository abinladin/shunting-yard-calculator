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

    #tests
    print(tokenizer("11  + 2 -   3", list(operator_to_precedence.keys())))
