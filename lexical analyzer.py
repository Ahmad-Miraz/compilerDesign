keywords = ['auto', "break", "case", "char", "const", "continue", "default", "double", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typeof", "union", "unsigned", "void", "volatile", "while", "do", "else"]
keywordsFlag = 0
keywordsList = []

builtin_functions = ['scanf', 'printf']
builtin_functionsFlag = 0
builtin_functionsList = []

parentheses = ['()', '{}', '[]']
parenthesesFlag = 0
parenthesesList = []

punctuations = [';', ':', ',']
punctuationsFlag = 0
punctuationsList = []

arithmetic_operators = ['+', '-', '*', '/', '=']
arithmetic_operatorsFlag = 0
arithmetic_operatorsList = []

logical_operator = ['>', '>=', '<', '<=', '==', '!=']
logical_operatorFlag = 0
logical_operatorList = []

identifierFlag = 0
identifierList = []

numericFlag = 0
numericList = []

# tracker = 0

line = input('Enter your code here: ')

lexemes = line.split(" ")

for i in range(len(lexemes)):
    if lexemes[i] == '//':
        del lexemes[i:]
        break
    if lexemes[i] == '/*':
         del lexemes[lexemes.index('/*'): lexemes.index('*/')]
         break


def paranthesis_checker(lexems, parenthesesFlag, parenthesesList):
    for i in range( len(lexemes)):
        if lexemes[i] == '(':
            for j in range(i+1, len(lexemes)):
                if lexemes[j] == ')':
                    if '()' not in parenthesesList:
                        parenthesesFlag += 1
                        parenthesesList = parenthesesList + ['()']

        elif lexemes[i] == '{':
            for j in range(i+1, len(lexemes)):
                if lexemes[j] == '}':
                    if '{}' not in parenthesesList:
                        parenthesesFlag += 1
                        parenthesesList = parenthesesList + ['{}']

        elif lexemes[i] == '[':
            for j in range(i+1, len(lexemes)):
                if lexemes[j] == ']':
                    if '[]' not in parenthesesList:
                        parenthesesFlag += 1
                        parenthesesList = parenthesesList + ['[]']
    return parenthesesList, parenthesesFlag

for i in lexemes:
    if i in keywords:
        if i not in keywordsList:
            keywordsList = keywordsList + [i]
            keywordsFlag += 1

    elif i in builtin_functions:
        if i not in builtin_functionsList:
            builtin_functionsList = builtin_functionsList + [i]
            builtin_functionsFlag += 1


    elif i in punctuations:
        if i not in punctuationsList:
            punctuationsList = punctuationsList + [i]
            punctuationsFlag += 1

    elif i in arithmetic_operators:
        if i not in arithmetic_operatorsList:
            arithmetic_operatorsList = arithmetic_operatorsList + [i]
            arithmetic_operatorsFlag += 1

    elif i in logical_operator:
        if i not in logical_operatorList:
            logical_operatorList = logical_operatorList + [i]
            logical_operatorFlag += 1

    elif i.isidentifier():
        if i not in identifierList:
            identifierList = identifierList + [i]
            identifierFlag += 1

    elif i.isnumeric():
        if i not in numericList:
            numericList = numericList + [i]
            numericFlag += 1

    elif i == '(' or i == '{' or i == '[':
        parenthesesList, parenthesesFlag = paranthesis_checker(i, parenthesesFlag, parenthesesList)

   


if keywordsFlag != 0:
    print("Keyword (" + str(keywordsFlag) + ") : " + ','.join(keywordsList))

if builtin_functionsFlag != 0:
    print("Builtin functions (" + str(builtin_functionsFlag) + ") : " + ','.join(builtin_functionsList))

if parenthesesFlag != 0:
    print("Parentheses (" + str(parenthesesFlag) + ") : " + ','.join(parenthesesList))

if punctuationsFlag != 0:
    print("Punctuations (" + str(punctuationsFlag) + ") : " + ','.join(punctuationsList))

if arithmetic_operatorsFlag != 0:
    print("Arithmetic Operators (" + str(arithmetic_operatorsFlag) + ") : " + ','.join(arithmetic_operatorsList))

if logical_operatorFlag != 0:
    print("Logical Operator (" + str(logical_operatorFlag) + ") : " + ','.join(logical_operatorList))

if identifierFlag != 0:
    print("Identifier (" + str(identifierFlag) + ") : " + ','.join(identifierList))

if numericFlag != 0:
    print("Constant (" + str(numericFlag) + ") : " + ','.join(numericList))