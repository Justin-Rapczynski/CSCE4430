#Created by Justin Rapczynski, Long Nguyen, and Oliver Velez
# Create all possible Binary trees with N internal Nodes
def bin(n):
    if n == 0:
        yield '0'
    else:
        for k in range(0, n):
            for l in bin(k):
                for r in bin(n - 1 - k):
                    yield (l, r)


# Declare how many internal Nodes there are
n = 4

# list that will hold all of the possible Binary Trees
All_Possibilities = []
operators = ['^']

# adding all the possibilities created by bin() to our list
for value in (bin(n)):
    value = str(value).replace(',', '^')
    value = str(value).replace(' ', '')
    value = str(value).replace("'", "")
    All_Possibilities.append(value)


# Using two for loops we convert the given tree into PostFix notation and store it on a txt file called postfix.txt
def to_postfix(infix: str) -> str:
    """
    This function convert infix form of a binary tree to postfix form
    :param infix: a string represent a binary tree in infix form
    :return: a string represent the same binary tree in postfix form
    """
    stack = []
    postfix = []            #result list
    for char in infix:
        if char == '0':                         #if the character is operand, push it to the result list
            postfix.append(char)
        else:
            if char == '^':                     #if the character is the operator, push it to the stack
                stack.append(char)
            elif char == '(':                   #if the character is the open parenthesis, push it to the stack
                stack.append(char)
            elif char == ')':                   #if the character is the close parenthesis, push everything in the stack
                operator = stack.pop()          #to the result list until we see the open parenthesis
                while operator != '(':
                    postfix.append(operator)
                    operator = stack.pop()

    while len(stack) != 0:                      #in case the stack has leftover, push everything left to the result list
        postfix.append(stack.pop())

    return ''.join(postfix)


def to_infix(rfPostfix: str) -> str:
    """

    This function convert postfix form of a binary tree to infix form
    :param postfix: a string represent a binary tree in postfix form
    :return: a string represent the same binary tree in infix form
    """
    stack = []
    for char in rfPostfix:
        if char == '0':                 #if the character is an operand, push it to the stack
            stack.append(char)
        elif char == '^':               #if the character is the operator:
            operand1 = stack.pop()      #pop out the operands from the stack
            operand2 = stack.pop()
            expression = '(' + operand2 + char + operand1 + ')'      #and put the character(operator) between them
            stack.append(expression)    #then push the expression back to the stack

    return ''.join(stack)


postfix = []
for elem in All_Possibilities:
    postfix.append(to_postfix(elem))


# Write all postfix posibilities to the txt file
with open('postfix.txt', 'w+') as fp:
    for elements in postfix:
        fp.write(elements)
        fp.write("\n")

rfPostfix = []
#rfPostfix = open('postfix.txt', 'r').read().split('\n')

#Take data from the postfix file and create a variable that holds the data read directly from the postfix.txt
with open('postfix.txt', 'r') as fileobj:
    for row in fileobj:
        rfPostfix.append( row.rstrip('\n') )
print("POSTFIX: ")
print(rfPostfix)

print('-' * 100)

infix = []
for elem in postfix:
    infix.append(to_infix(elem))
print("INFIX: ")
print(infix)

print('-' * 100)
for value in All_Possibilities:
    print(value)
#Compares data written to the .txt file to the data recieved from the .txt file
print("Does the tree read back from the file correspond to the same tree that was written out? (True = yes False = no")
print(infix == All_Possibilities)
