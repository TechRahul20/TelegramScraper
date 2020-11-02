#Imports#
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import pandas as pd
import csv
import details as ds

#Login details#
api_id = ds.apiID
api_hash = ds.apiHash
phone = ds.number
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
target_entity=groups[int(g_index)]

print('Fetching forwards...')

async def main():
    l = []
    async for message in client.iter_messages(target_entity):

        if message.forward is not None:
            try:
                id = message.forward.original_fwd.from_id
                if id is not None:
                    ent = await client.get_entity(id)
                    print(ent.title)
                    l.append([ent.title,id,target_entity.title,target_entity.id])
            except:
                print("An exception occurred")

    df = pd.DataFrame(l, columns = ['From','From ID','To', 'To ID'])
    df.to_csv('forwards_data.csv')

with client:
    client.loop.run_until_complete(main())

print('Forwards scraped successfully.')

again = input('Do you want to scrape more groups? (y/n)')
if again == 'y':
    print('Restarting...')
    exec(open("forwards.py").read())
else:
    pass

launcher = input('Do you want to return to the launcher? (y/n)')
if launcher == 'y':
    print('Restarting...')
    exec(open("launcher.py").read())
else:
    print('Thank you for using the Telegram scraper.')
