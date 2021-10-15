import discord
from discord.ext import commands, tasks
import asyncio
import os
from candy import sugar #for flask server
import cogs
from richhelp import HelpCommand 
#from dotenv import dotenv_values

#config = dotenv_values(".env")
client = commands.Bot(command_prefix=".", help_command=HelpCommand(), owner_ids=[], case_insensitive=True, intents=discord.Intents.all()) #owner_ids=[] (to use is_owner only commands

@client.event
async def on_ready():
	game = discord.Game("with the API")
	await client.change_presence(status=discord.Status.dnd, activity=game)
	for filename in os.listdir("./cogs"):
		if filename.endswith(".py"):
			client.load_extension(f"cogs.{filename[:-3]}")
			print("Cogs Loaded!")
	print("Bot is ready and logged in {}".format(client.user))

sugar()
token = os.environ['TOKEN']
client.run(token)
