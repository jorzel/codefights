"""
Medium

Codewriting

4000

Each World Cup fan has his/her own Fan Identificator which is presented as a unique 8-digit number. These identificators are used to control the fans coming for the match.

Fan IDs are stored in files that have path of the format /root/devops/{location1}/.../{locationN}/fan.info, according to geolocation. For example, the file /root/devops/russia/moscow/center/fan.info contains all the russian fan IDs from center of moscow. There are no limits for the depth of the file path. It is guaranteed that every fan ID appears in one file only.

Your task is to create a system for fan control.

You can invite fans from a separate geolocation or ban them because of their inadmissible behavior. File /root/devops/invite.info contains the locations from where the fans are invited to the match. File /root/devops/ban.info contains the locations, from where the fans are banned.

Every location is written in a separate line, subregions are separated by .. Every location corresponds to a file system path.

The locations in the invitation list or ban list are recursive. This means that you can invite all fans in a subdirectory without writing the full path to the fan.info file.

For example, if there are 2 files of fan IDs with the paths /root/devops/russia/moscow/center/fan.info and /root/devops/russia/moscow/east/fan.info, and the invitation has a line russia.moscow, you should invite fans from both files.

The locations in the invitation or ban lists are nested. This means you can invite all fans from a directory, but ban fans from its subdirectory.

For example, if there are 2 files of fan IDs with the paths /root/devops/russia/moscow/center/fan.info and /root/devops/russia/moscow/east/fan.info, and the invitation has a line russia.moscow, and the ban list has russia.moscow.east, you should invite fans from /root/devops/russia/moscow/center/fan.info only.

For the simplicity, it is impossible to invite and to ban the same location.

The output for this task is a list of the fan IDs according to invitations and bans sorted lexicographically.

Example

Consider the following files on your computer:

/root/devops/russia/moscow/center/b1/fan.info
/root/devops/russia/moscow/center/b2/fan.info
/root/devops/russia/moscow/east/fan.info
/root/devops/invite.info
/root/devops/ban.info
/root/devops/russia/moscow/center/b1/fan.info contains the following information:

00000001
00000002
00000003
/root/devops/russia/moscow/center/b2/fan.info contains the following information:

00000004
00000005
00000006
/root/devops/russia/moscow/east/fan.info contains the following information:

10000007
10000008
10000009
/root/devops/invite.info contains the following information:

russia.moscow.center
russia.moscow.east
/root/devops/ban.info contains the following information:

russia.moscow.center.b2
The output for this test should be as follows:

00000001
00000002
00000003
10000007
10000008
10000009
"""


import requests
import os
import mysql.connector

results = set()
ROOT = '/root/devops/'

def read_file(path):
    with open(path, 'r') as current:
        return [p.replace('\n', '') for p in current]

    
def get_content(location, invites, bans):
    dir_content = os.listdir(location)
    for el in dir_content:
        if el not in ('ban.info', 'invite.info'):
            path = os.path.join(location, el) 
            if os.path.isdir(path):
                get_content(path, invites, bans)
            else:
                encoded = path.split(ROOT)[-1].replace('/', '.').replace('.fan.info', '')
                for i in invites:
                    if i in encoded and encoded not in bans:
                        for _id in read_file(path):
                            results.add(_id)


get_content(ROOT, 
            read_file(os.path.join(ROOT, 'invite.info')),
            read_file(os.path.join(ROOT, 'ban.info')))
for p in sorted(results):
    print p

