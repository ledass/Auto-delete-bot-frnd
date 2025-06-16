from time import time 
from plugins.info import *
from plugins.database import *
from subprocess import Popen
from pyrogram import Client, filters

plugins=dict(root="plugins")

User = Client("auto-delete-user",
              session_string=SESSION)

@User.on_message(filters.chat(CHATS))
async def delete(user, message):
    try:
       if bool(WHITE_LIST):
          if message.from_user.id in WHITE_LIST:
             return 
       if bool(BLACK_LIST):
          if message.from_user.id not in BLACK_LIST:
             return
       _time = int(time()) + TIME 
       save_message(message, _time)
    except Exception as e:
       print(str(e))

#==========================================================

Popen(f"gunicorn plugins.server:app --bind 0.0.0.0:{PORT}", shell=True)
Popen("python3 -m plugins.delete", shell=True)
User.run()
