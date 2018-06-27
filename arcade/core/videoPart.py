"""
You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have already watched.

Example

For part = "02:20:00" and total = "07:00:00", the output should be
videoPart(part, total) = [1, 3].

You have watched 1 / 3 of the whole video.
"""


from fractions import Fraction

def get_seconds(t):
    hours, minutes, seconds = t.split(':')
    return int(seconds) + 60 * int(minutes) + 3600 * int(hours)

def videoPart(part, total):
    f = Fraction(get_seconds(part), get_seconds(total))
    return [int(f.numerator), int(f.denominator)]
