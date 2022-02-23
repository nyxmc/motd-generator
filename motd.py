import os

line1 = "           ❂ <bold><gradient:#00158c:#7b8ae3>Dark Moon SMP</gradient></bold> ❂ <white>[ 1.18.1 ]</white>"

with open("motd.txt", "r") as f:
    lines = f.readlines()

for sentence in lines:
    line2 = f"<yellow>{sentence.rstrip()}</yellow>"
    obj = '    {' + os.linesep + '        "line1"="' + line1 + '"' + os.linesep + '        "line2"="' + line2 + '"' + os.linesep + '    },'
    print(obj)
    
