from telethon import TelegramClient
from telethon import utils
import pandas as pd
import details as ds

#Login details#
api_id = ds.apiID
api_hash = ds.apiHash
phone = ds.number
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print('Welcome to channel forward scraper')
print('This tool will scrape a Telegram channel for all forwarded messages and their original source.')

while True:
    try:
        channel_name = input("Please enter a Telegram channel name:\n")
        print(f'You entered "{channel_name}"')
        answer = input('Is this correct? (y/n)')
        if answer == 'y':
            print('Scraping forwards from', channel_name, '...')
            break;
    except:
            continue

async def main():
    l = []
    async for message in client.iter_messages(channel_name):

        if message.forward is not None:
            try:
                id = message.forward.original_fwd.from_id
                if id is not None:
                    ent = await client.get_entity(id)
                    print(ent.title)
                    l.append([channel_name, ent.title])
            except:
              print("An exception occurred")

    df = pd.DataFrame(l, columns = ['From', 'To'])
    df.to_csv('edgelist.csv')

with client:
    client.loop.run_until_complete(main())

print('Forwards scraped successfully.')

next1 = input('Do you also want to scrape forwards from the discovered channels? (y/n)')
if next1 == 'y':
    print('Scraping forwards from channels discovered in', channel_name, '...')
    async def new_main():
        df = pd.read_csv('edgelist.csv')
        df = df.To.unique()
        l = []
        for i in df:
            async for message in client.iter_messages(i):
                if message.forward is not None:
                    try:
                        id = message.forward.original_fwd.from_id
                        if id is not None:
                            ent = await client.get_entity(id)
                            print(ent.title)
                            l.append([i, ent.title])
                    except:
                        print("An exception occurred")
            print("# # # # # # # # # # Next channel: ", i, "# # # # # # # # # #")
        df = pd.DataFrame(l, columns = ['From', 'To'])
        df.to_csv("ecofash_net.csv")

    with client:
        client.loop.run_until_complete(new_main())
    print('Forwards scraped successfully.')
else:
    pass

again = input('Do you want to scrape more channels? (y/n)')
if again == 'y':
    print('Restarting...')
    exec(open("channels.py").read())
else:
    pass

launcher = input('Do you want to return to the launcher? (y/n)')
if launcher == 'y':
    print('Restarting...')
    exec(open("launcher.py").read())
else:
    print('Thank you for using the Telegram scraper.')
