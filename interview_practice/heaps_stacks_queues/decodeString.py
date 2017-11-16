"""
Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.

Example

For s = "4[ab]", the output should be

decodeString(s) = "abababab";

For s = "2[b3[a]]", the output should be

decodeString(s) = "baaabaaa";

For s = "z1[y]zzz2[abc]", the output should be

decodeString(s) = "zyzzzabcabc".
"""


def mulitply_string(number, string):
    return number * string

def decodeString(s):
    string_stack = ['']
    num_stack = []

    i = 0
    while i < len(s):
        if s[i] == '[':
            i += 1
            continue
        elif s[i].isdigit():
            number = [s[i]]
            i += 1
            while (s[i].isdigit()):
                number.append(s[i])
                i += 1
            number = int(''.join(number))
            num_stack.append(number)
            string_stack.append('')
        elif s[i] == ']':
            string = string_stack.pop()
            number = num_stack.pop()
            string_stack[-1] += mulitply_string(number, string)
            i += 1
        else:
            string_stack[-1] += s[i]
            i += 1
    return ''.join(string_stack)
