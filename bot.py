import os
import discord
import math

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	print(f'{client.user} has connected to discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("#!"):
		count = int(message.content.lstrip("#!"))
		for num in range(count):
			await message.channel.send(str(msg))

client.run(TOKEN)