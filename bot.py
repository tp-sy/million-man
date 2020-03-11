import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_CHANNEL')
try:
    GOAL = int(os.getenv('COUNT_GOAL'))
except ValueError:
    print("Count goal not a number")
    exit(0)

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to discord!')
    for channel in client.get_all_channels():
        if channel.name == CHANNEL:
            text_channel = channel
    if not text_channel:
        print(f"Unable to find channel called {CHANNEL} from {GUILD}")
        return
    last_msg_id = text_channel.last_message_id

    while 1:
        command = input(">>>")
        if command.lower() == "q":
            return
        elif command.lower() == "count":
            last_msg = await text_channel.fetch_message(last_msg_id)
            try:
                latest_number = int(last_msg.content)
            except ValueError:
                print(f"Latest message is not a number: {last_msg.content}")
                return
            print(f"Printing numbers in range: {latest_number}, {GOAL}")
            for num in range(latest_number, GOAL + 1):
                await text_channel.send(str(num))
            print(f"Finished printing numbers...")
        elif command.lower() == "dryrun":
            last_msg = await text_channel.fetch_message(last_msg_id)
            try:
                latest_number = int(last_msg.content)
            except ValueError:
                print(f"Latest message is not a number: {last_msg.content}")
                return
            print(f"(Dry) Printing numbers in range: {latest_number}, {GOAL}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("#!") and message.channel.name == CHANNEL:
        print(message.content)

client.run(TOKEN)
