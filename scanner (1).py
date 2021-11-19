
file = open('Tiny_Sample_Program.txt')

Reserved_Words = {'if': 'IF',
                  'then': 'THEN',
                  'else': 'ELSE',
                  'end': 'END',
                  'repeat': 'REPEAT',
                  'until': 'UNTIL',
                  'read': 'READ',
                  'write': 'WRITE',
                  'fact': 'FACTORIAL'}
Reserved_Words_key = Reserved_Words.keys()

Special_Symbols = {
    ':=': 'ASSIGNMENT',
    '<=': 'LESS|EQUAL',
    '>=': 'GREATER|EQUAL',
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MUL',
    '/': 'DIVISION',
    '<': 'LESS',
    '>': 'GREATER',
    ';': 'SEMICOLON',
    '(': 'OPEN_PARENTHESIS',
    ')': 'CLOSE_PARENTHESIS',
    '=': 'EQUALS',
    ':': 'COLON'}
Special_Symbols_key = Special_Symbols.keys()

TokensType = []
TokensVal = []
temp = ""
Number = 0
Identifier = ""
Tokens = []
sub_token=[]

def check(temp_token):
    # symbol = None
    flag=False
    temp_list = []
    found_index =100
    for s in Special_Symbols:
        index = temp_token.find(s)
        if index > -1:  # symbol is found
            flag=True
            if index < found_index:
                found_index = index
    if flag:
        if found_index == len(temp_token)-1:
            symbol = temp_token[found_index]
        elif temp_token[found_index + 1] in Special_Symbols:
            symbol = temp_token[found_index:found_index + 2]

        else:
            symbol = temp_token[found_index]

        temp_list = temp_token.split(symbol, 1)

        sub_token.append(temp_list[0])
        sub_token.append(symbol)

        check(temp_list[1])

    if not flag:
        sub_token.append(temp_token)
    return sub_token



dataFlag = False
a = file.read()
program = a.split("\n")

for line in program:
    Tokens = line.split(' ')
    temp = "continue"
    i = -1

    for Token in Tokens:
        i = i+1
        if Token == "{" or temp == "{" or Token.find("{") != -1:
            temp = "{"
            if Token == "}":
                temp = "continue"
                continue
        if temp == "continue":


            if Token in Special_Symbols_key:
                TokensVal.append(Tokens[i])
                TokensType.append(Special_Symbols.get(Tokens[i]))
            elif Token in Reserved_Words_key:
                TokensVal.append(Tokens[i])
                TokensType.append(Reserved_Words.get(Tokens[i]))
            else:

                sub_tokens = check(Tokens[i])
                for item in sub_tokens:

                    if item in Special_Symbols:
                        TokensVal.append(item)
                        TokensType.append(Special_Symbols.get(item))

                    elif len(item) > 0 and item[0].isalpha():  # if first char is a letter
                        Identifier = item
                        TokensVal.append(Identifier)
                        TokensType.append("IDENTIFIER")

                    elif len(item) > 0 and not(item[0].isalpha()):
                        Number = item
                        TokensVal.append(Number)
                        TokensType.append("NUMBER")
                sub_token = []




# write in another txt file "TokensTable.txt"
fw = open('TokensTable.txt', "w")
n = len(TokensVal)
i = 0
while i < n:
    fw.write(TokensVal[i] + ' , ' + TokensType[i] + '\n')
    i += 1
fw.close()

dataFlag = False

# print("done for check ...")



