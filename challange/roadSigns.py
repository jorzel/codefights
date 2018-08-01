"""

Medium

Codewriting

2000

Summer road trip time! You and your friends are driving all the way to Banff National Park for a camping trip in the woods.

While staring out of the car window, your friend started reading some road signs in a strange way to break the silence. The messages were all weird, they were nothing like what the road sign wrote when he read it out loud!

Given a sign in its more readable form with sign[i] being one section of the sign, guess what your friend will read out.

Yes, this is a reverse challenge, enjoy!

Example

For sign = ["You matter.", "Don't give up."], the output should be roadSigns(sign) = "You don't matter. Give up.". What a nice message.
"""

def roadSigns(sign):
    sign = [(len(line.split()), line.split()) for line in sign]
    n = max(sign)[0]
    output = ""
    for i in range(n):
        for size, line in sign:
            if size > i:
                if output and output[-1] in ('.', '?', '!'):
                    word = line[i].capitalize()
                else:
                    word = line[i].lower()
                if word[0] not in ('!', '?', '.'):
                    output += " "
                output += word 
    return output[1:2].upper() + output[2:]