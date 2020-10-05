import sys
sys.setrecursionlimit(10000)

def recursive_reducer(string, position):
    if len(string) == 0:
        return 'Empty String'

    if position + 1 >= len(string):
        return string

    if string[position] == string[position + 1]:
        aux = string[:position]
        aux2 = string[position+2:]
        string = f'{aux}{aux2}'
        position = 0
    else:
        position += 1

    return recursive_reducer(string, position)

def superReducedString(s):
    string = recursive_reducer(s, 0)
    return string

# if __name__ == '__main__':
def main(s):
    # s = input()

    return superReducedString(s)

"""
Input:
    aaabccddd
Output:
    abd

Input:
    aa
Output:
    Empty String

Input:
    baab
Output:
    Empty String

Input:
    acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj
Output:
    acdqgacdqj
"""
