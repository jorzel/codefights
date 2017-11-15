"""
Correct variable names consist only of Latin letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
For name = "2w2", the output should be
variableName(name) = false.
"""


def variableName(name):
    for i, s in enumerate(name):
        if s.isalpha() or s == '_':
            pass
        elif s.isdigit() and i != 0:
            pass
        else:
            return False
    return True
