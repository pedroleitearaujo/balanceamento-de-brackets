#!/bin/python3
# malumriano
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    types_brackets = [
        {
            'open': '{',
            'close': '}',
        },
        {
            'open': '[',
            'close': ']',
        },
        {
            'open': '(',
            'close': ')',
        }
    ]

    last_to_close = []
    is_correct = 'YES'
    for ch in brackets:
        for type_bracket in types_brackets:
            if (ch == type_bracket['open']):
                last_to_close.append(type_bracket['close'])
            elif (len(last_to_close) > 0 and ch == type_bracket['close']):
                if (type_bracket['close'] == last_to_close[len(last_to_close) - 1]):
                    last_to_close.pop()
                else:
                    is_correct = 'NO'

    return is_correct 


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')