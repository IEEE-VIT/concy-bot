import discord
from discord.ext import commands
import asyncio
import time

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")

@client.command(aliases=["stopwatch", "start-stopwatch"])
async def stopwach(ctx):
    #stopwatch
     
    
    pass