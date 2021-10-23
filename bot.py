import discord, os
from discord.ext import commands
from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
@commands.is_owner() #Only Owner of the bot can run this command
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner() #Only Owner of the bot can run this command
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    # This command stops the working of the given extension till is is reloaded
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(config["token"])
