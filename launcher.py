from telethon.sync import TelegramClient
from telethon import TelegramClient

#launcher code#
print('Welcome to I NEED A NAME FOR THIS:')
print('DESCRIPTION')

li = ['Scrape group members', 'Scrape forwards from chats you are in', 'Scrape forwards from a channel']

def display(li):
    for idx, tables in enumerate(li):
        print("%s. %s" % (idx+1, tables))

def get_list(li):
    choose = int(input("\nPick a number:"))-1
    if choose < 0 or choose > (len(li)-1):
        print('Invalid Choice')
        return ''
    return li[choose]

display(li)
choice = (get_list(li))

print('Loading', choice,'...')

if choice == 'Scrape group members':
    print('Launching group member scraper')
    exec(open("groups.py").read())
elif choice == 'Scrape forwards from chats you are in':
    print('Launching chat forward scraper')
    exec(open("forwards.py").read())
elif choice == 'Scrape forwards from a channel':
    print('Launching channel forward scraper')
    exec(open("channels.py").read())
