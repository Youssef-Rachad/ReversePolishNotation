import rpn

expression = rpn.str_to_polska("1 + 1")
print(expression)
result = rpn.polska(expression)
print(result)
