def doIt(elemento1, elemento2,  operacao):
        if operacao == 'SUM':
            return elemento1 + elemento2
        elif operacao == 'SUB':
            test = elemento1 - elemento2
            return test
        elif operacao == 'MULT':
            test = elemento1 * elemento2
            return test
        elif operacao == 'DIV':
            test = elemento1 / elemento2
            return test

input = open('input.txt')

stack = []

line = 0

while True:
    line = input.readline()
    splitedLine = line.split()
    if len(splitedLine) == 2:
        stack.append(int(splitedLine[1]))
    elif splitedLine[0] == 'PRINT':
        print(stack.pop())
        break
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(doIt(a, b, splitedLine[0]))
