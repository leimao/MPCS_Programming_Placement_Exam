# This is a crazy test problem.
# It is not difficult at all but it consumes almost all of my test time!

import sys

fhand = sys.stdin
lines = fhand.readlines()

tokens = lines[0].strip().split(' ')

operators = ['+', '*', '==', 'and', 'or']
booleans = ['true', 'false']

# Reformat tokens
for i in xrange(len(tokens)):
	if (tokens[i] not in operators) and (tokens[i] not in booleans):
		tokens[i] = int(tokens[i])
	elif tokens[i] in booleans:
		if tokens[i] == 'true':
			tokens[i] = True
		else:
			tokens[i] = False

def reverse_polish(tokens):
	stack = list()
	for token in tokens:
		if token not in operators:
			stack.append(token)
		else:
			if len(stack) < 2:
				return "SYNTAX ERROR"
			operand_1 = stack.pop()
			operand_2 = stack.pop()
			if type(operand_1) != type(operand_2):
				return "TYPE ERROR"
			if (token in ['+', '*', '==']) and (type(operand_1) == bool):
				return "TYPE ERROR"
			if (token in ['and', 'or']) and (type(operand_1) == int):
				return "TYPE ERROR"
			if token == '+':
				stack.append(operand_1 + operand_2)
			if token == '-':
				stack.append(operand_1 - operand_2)
			if token == '*':
				stack.append(operand_1 * operand_2)
			if token == '==':
				stack.append(operand_1 == operand_2)
			if token == 'and':
				stack.append(operand_1 and operand_2)
			if token == 'or':
				stack.append(operand_1 or operand_2)

	if len(stack) != 1:
		return "SYNTAX ERROR"
	else:
		return stack[0]

# Reformat result
result = reverse_polish(tokens)
if type(result) == bool:
	if result == True:
		result = 'true'
	else:
		result = 'false'

print result


