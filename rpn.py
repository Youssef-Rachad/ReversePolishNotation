import stack
## Reverse Polish notation is a postfix method to evaluate expressions
# https://www.mathblog.dk/reverse-polish-notation/

# Only binary operators for now
operators = ['+', '-', '*', '/']

def str_to_polska(expression: str) -> list:
    return ["1","1","+"]
    

def evaluate(op1: str, op: str, op2: str) -> str:
    # Parse a binary operation from scratch (so long)
    try:
        float(op1)
    except ValueError:
        return "[Error] Invalid operand: "+op1+"\n"
    try:
        float(op2)
    except ValueError:
        return "[Error] Invalid operand: "+op2+"\n"
    try:
        op in operators
    except ValueError:
        return "[Error] Invalid operator: "+op+"\n"
    if op == '+':
        return float(op2) + float(op1)
    if op == '-':
        return float(op2) - float(op1)
    if op == '*':
        return float(op2) * float(op1)
    if op == '/':
        return float(op2) / float(op1)

def polska(expression: list):
    stak = stack.Stack()
    for element in expression:
        if element in operators:
            operand_two = stak.pop()
            operand_one = stak.pop()
            result = evaluate(operand_one, element, operand_two)
            stak.push(result)
        elif element.isnumeric():
            stak.push(element)
    return stak.pop()
