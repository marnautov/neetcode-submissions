class Solution:
    def calculate(self, s: str) -> int:
        tokens = []

        num = 0
        for char in s:
            if char.isspace():
                continue

            if char.isdigit():
                num = num * 10 + int(char)
            else:
                tokens.append(num)
                tokens.append(char)
                num = 0

        tokens.append(num)

        stack = []
        operation = None
        for item in tokens:
            if item in ['+', '-', '*', '/']:
                operation = item
                continue

            if operation == '*':
                stack.append(stack.pop() * item)
            elif operation == '/':
                stack.append(stack.pop() // item)
            else:
                if operation in ('+', '-'):
                    stack.append(operation)
                stack.append(item)

        operation = None
        result = 0
        
        for item in stack:
            if item in ['+', '-']:
                operation = item
            else:
                if operation == '+':
                    result = result + item
                elif operation == '-':
                    result = result - item
                else:
                    result = item

        return result



        