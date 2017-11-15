"""
You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. It is guaranteed that the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. The results string should not contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".
"""


def reverseParentheses(s):
    chars = list(s)
    open_brackets_index = []
    for i, c in enumerate(chars):
        if c == '(':
            open_brackets_index.append(i)
        elif c == ')':
            j = open_brackets_index.pop()
            chars[j:i] = chars[i:j:-1]
    return ''.join(c for c in chars if c not in '()')
