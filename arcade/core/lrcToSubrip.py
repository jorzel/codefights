"""
During your most recent trip to Codelandia you decided to buy a brand new CodePlayer, a music player that (allegedly) can work with any possible media format. As it turns out, this isn't true: the player can't read lyrics written in the LRC format. It can, however, read the SubRip format, so now you want to translate all the lyrics you have from LRC to SubRip.

Since you are a pro programmer (no noob would ever get to Codelandia!), you're happy to implement a function that, given lrcLyrics and songLength, returns the lyrics in SubRip format.

Example

For

lrcLyrics = ["[00:12.00] Happy birthday dear coder,",
             "[00:17.20] Happy birthday to you!"]
and songLength = "00:00:20", the output should be

lrc2subRip(lrcLyrics, songLength) = [
  "1",
  "00:00:12,000 --> 00:00:17,200",
  "Happy birthday dear coder,",
  "",
  "2",
  "00:00:17,200 --> 00:00:20,000",
  "Happy birthday to you!"
]
"""

def convert(t):
    parts = t.split(':')
    seconds = parts[-1].split('.')
    if len(seconds) == 1:
        miliseconds = '000'
    elif len(seconds) == 2:
        miliseconds = seconds[-1] + '0'
    seconds = seconds[0]

    if len(parts) == 2:
        hours = 0
        minutes = int(parts[0])
    elif len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
    if minutes >= 60:
        minutes -= 60
        hours += 1

    return "{0}:{1}:{2},{3}".format(str(hours).zfill(2), str(minutes).zfill(2), seconds, miliseconds)

def parse_line(line):
    pattern = re.compile("\[(.+)\](.*)")
    matched = re.match(pattern, line)
    return convert(matched.group(1)), matched.group(2).lstrip()

def lrc2subRip(lrcLyrics, songLength):
    _length = len(lrcLyrics)
    results = []

    _time = {}
    _text = {}
    for i in range(_length - 1):
        results.append(str(i + 1))
        if i not in _time:
            _time[i], _text[i] = parse_line(lrcLyrics[i])
            
        if i + 1 not in _time:
            _time[i+1], _text[i+1] = parse_line(lrcLyrics[i+1])
        results.append("{0} --> {1}".format(_time[i], _time[i+1]))
        results.append(_text[i])
        results.append("")
    results.append(str(_length))
    results.append("{0} --> {1}".format(_time[_length-1], convert(songLength)))
    results.append(_text[_length-1])
    return results