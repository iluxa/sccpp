#!/usr/bin/python

import string
import random
import re

sccp = open('sccp.conf', 'w')
sccpsimple = open('sccp.conf.simple', 'w')
sccpdial = open('sccp.dialplan', 'w')

def randomMAC():
    mac = [ 0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]
    return ''.join(map(lambda x: "%02X" % x, mac))

line_instance = 1000
count = 0

sccp.write('[lines]\n')
while (count < 500):
 sccp.write('[' + str(line_instance) + ']\n')
 sccp.write('cid_num=' + str(line_instance) + '\n')
 sccp.write('cid_name=' + ''.join(random.choice(string.ascii_lowercase) for _ in xrange(5)) + '\n')
 sccp.write('language=fr_CA\n')
 sccp.write('\n')

 line_instance += 1
 count += 1 


line_instance = 1000
count = 0

sccpdial.write('[xivo-extrafeatures]\n')
sccpdial.write('[default]\n')

sccp.write('[devices]\n')
while (count < 500):
 mac = str(randomMAC())
 sccp.write('[SEP' + mac + ']\n')
 sccp.write('devices=' + str(mac) + '\n')
 sccp.write('line=' + str(line_instance) + '\n')
 sccp.write('\n')

 sccpsimple.write('SEP' + mac + ',' + str(line_instance) + '\n')

 sccpdial.write('exten => ' + str(line_instance) + ',1,Dial(SCCP/' + str(line_instance) + ')\n');
# sccpws.write('skaro-dev, f, l, fr_FR, ' + str(line_instance) + ', default, sccp, 0, 0, 0, ' + ':'.join(re.findall('..',mac))  + '\n');

 line_instance += 1
 count += 1
