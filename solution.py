def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    longest = 0

    for index, char in enumerate(s):
        if char == "(":
            stack.append(index)
        else:
            stack.pop()

            if not stack:
                stack.append(index)
            else:
                current_length = index - stack[-1]
                if current_length > longest:
                    longest = current_length

    return longest


if __name__ == "__main__":
    value = input("Enter a parentheses string: ").strip()
    print(longest_valid_parentheses(value))