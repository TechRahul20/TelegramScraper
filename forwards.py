#Imports#
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

#Login details#
api_id = YOUR API ID
api_hash = 'YOUR API HASH'
phone = 'YOUR PHONE'
client = TelegramClient(phone, api_id, api_hash)

#Check authorisation#
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    groups.append(chat)

print('List of chats:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]

print('Fetching forwards...')
all_participants = []
all_participants = client.iter_messages(target_group)

print('Saving In file...')
with open("forwards.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['forward id','group','group id'])
    for user in all_participants:
        if user.forward is not None:
            try:
                id = user.forward.original_fwd.from_id
                if id is not None:
#                    ent = await client.get_entity(id)
                    print(ent.title)
                    l.append([target_group, ent.title])
            except:
              print("An exception occurred")
            writer.writerow([id,target_group.title, target_group.id])
print('Forwards scraped successfully.')

#async def main():
    # Getting information about yourself
#    l = []
    # You can print the message history of any chat:
#    async for message in client.iter_messages('CHANNEL NAME'):
