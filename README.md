# TelegramScraper

Tool for using Telegram to investigate shady goings on.

## Installation

1. Download all files and save to directory of choice.

2. Ensure pandas and telethon are installed.

```bash
pip install pandas
pip install telethon
```

3. Obtain your Telegram API details from [my.telegram.org][1] (further instructions to be added here).

4. In terminal, navigate to the installation directory (eg, desktop) and run setup.py 

```bash
cd Desktop
python3 setup.py
```

5. Executing the setup.py file will walk you through the Telegram API login and prepare the toolkit with your details.

n.b: Currently there is no easy installation, however, I'm working on properly packaging everything to make this straightforward for non-technical users.

## Usage

Upon installation completion, you will be able to launch the toolkit from launcher.py

```bash
cd Desktop
python3 launcher.py
```

The launcher will guide you through each of the tools. Here is an overview.

1. _Scrape group members_
Scrapes all group members from a Telegram group you are part of. Exports as a .CSV containing the username (when available), user id, name, group name and group ID. The file is named after the group.

2. _Scrape forwards from chats you are in_
Scrapes all forwards from a chat you are following. Saves from, from ID, to and to ID to _forwards_data.csv_.

The tool currently doesn't have the expanded feature of scraping from all discovered groups, but these will be added.

3. _Scrape forwards from a channel_
Scrapes all forwards from any channel you specify and can then scrape forwards from all the discovered channels for a larger network map. This second feature takes a long time to run, but is worthwhile for a broader analysis.

Currently only scrapes from user and to user then saves to _ef_edgelist.csv_.

## Upcoming updates

1. An option to export all data (from user, from user ID, to user, and to ID) OR simply exporting an edgelist for direct analysis.

2. Updating all save files to generate unique names for each group/chat scraped.

## Known bugs

1. Sometimes, when using _scrape group members_, returning to the launcher, then selecting _scrape forwards from chats you are in_, the toolkit will crash. This is an API error and can be avoided by restarting the launcher.

2. _Scrape forwards from chats you are in_ displays an error message when you try to pull from _Groups_ rather than _Channels_. Working on a fix to omit groups from the generated list.

## Feedback

Please send all feedback either to ([@jordanwildon][2]) on Twitter, or to jordanwildon@protonmail.com

## License

This project is still being tested and is not currently licensed. Please contact @JordanWildon on Twitter, or email jordanwildon@protonmail.com for usage information and restrictions.

## Credits

All tools created by Jordan Wildon ([@jordanwildon][2]) and Alex Newhouse ([@AlexBNewhouse][3]).

[1]: <https://my.telegram.org/auth?to=apps> "Telegram API"
[2]: <twitter.com/jordanwildon> "@jordanwildon"
[3]: <twitter.com/AlexBNewhouse> "@AlexBNewhouse"
