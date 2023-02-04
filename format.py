import re
# Flatten CTS
f1 = open('logs/CTS/CTS_4k_alter.log', 'r')
f2 = open('logs/CTS/CTS_4k.log', 'w')
s = ""
for line in f1.readlines():
    if re.search('\[[0-9]\]\[\S+\]', line):
        if s != "":
            f2.write(s + '\n') 
        s = ""
    s = s + re.sub('\n','/n',line)
f2.write(s + '\n')
# Flatten HiBench
f1 = open('logs/HiBench/HiBench_4k_alter.log', 'r')
f2 = open('logs/HiBench/HiBench_4k.log', 'w')
s = ""
for line in f1.readlines():
    if re.search('\[[0-9]{2}:[0-9]{2}:[0-9]{2}\]', line):
        if s != "":
            f2.write(s + '\n') 
        s = ""
    s = s + re.sub('\n','/n',line)
f2.write(s + '\n')