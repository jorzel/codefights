"""
Medium

Codewriting

2000

Here is a little fun in a blank page and a colorful mind. Your 6 year old daughter is having fun writing words she sees around her. Sometimes from the newspaper, sometimes from TV, sometimes from books lying around the house.

The problem is, she is not really great with vertical alignment. Or maybe it was on purpose, who knows.

She wrote all the words in a zigzag pattern (in l lines, starting at the bottom line), disregarding all whitespace characters.

For example, the word HOSPITAL in 3 lines is now:

    S       A 
  O   P   T   L
H       I  
You decide it is a good idea to teach her how people would try to read it if she does not write in a single line.

Since this would normally be read from left to right, one line at a time, it would look like "SA", "OPTL", and "HI", so you show her the output "SAOPTLHI".

Examples

For t = "HOSPITAL" and l = 3, the output should be zigzagWords(t, l) = "SAOPTLHI"

For t = "my sweet daughter" and l = 3, the output should be zigzagWords(t, l) = "stgryweduhemeat"

Writing in a zigzag pattern and ignoring whitespaces, the text would look like this:

    s       t       g       r
  y   w   e   d   u   h   e
m       e       a       t
Reading from left to right, the lines concatenate to form the string "stgryweduhemeat"."""


def zigzagWords(t, l):
    if l == 1:
        return t
    t = t.replace(' ', '')

    output = ""
    up_indexes = range(l-1, len(t), 2*l - 2)
    down_indexes = range(0, len(t), 2*l - 2)
    up_len = len(up_indexes)
    down_len = len(down_indexes)
    length = up_len if up_len > down_len else down_len
    
    for j in range(l):
        first_pass = True
        for i in range(length):
            try:
                current_up = up_indexes[i] + j
            except IndexError:
                current_up = None
            try:
                current_down = down_indexes[i] + l - j - 1
            except IndexError:
                current_down = None

            if current_down  == current_up:
                output += t[current_up]
            else:
                if j == l - 1 and not first_pass:
                    pass
                else:
                    try:
                        output += t[current_down]
                    except (IndexError, TypeError):
                        pass
                try:
                    output += t[current_up]
                except (IndexError, TypeError):
                    pass
            first_pass = False
    return output