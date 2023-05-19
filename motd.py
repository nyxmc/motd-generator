import os

line1 = "           ❂ <bold><gradient:#00158c:#7b8ae3>Dark Moon SMP</gradient></bold> ❂ <white>[ 1.19.2 ]</white>"

with open("motd.txt", "r") as f:
    lines = f.readlines()

out = """
# MiniMOTD Main Configuration

# Enable server list icon related features
icon-enabled=false
# Enable MOTD-related features
motd-enabled=true
# The list of MOTDs to display
# 
# - Supported placeholders: {onlinePlayers}, {maxPlayers}
# - Putting more than one will cause one to be randomly chosen each refresh
motds=[
"""

for sentence in lines:
    if sentence.startswith("#"): continue

    out += '''
    {
        "line1"="%s"
        "line2"="<yellow>%s</yellow>"
    },''' % (line1, sentence.strip())


out += os.linesep + "]"

with open("main.conf", "w") as f:
    f.write(out)
