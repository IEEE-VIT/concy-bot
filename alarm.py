import discord
from discord.ext import commands
import asyncio
import time

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")


@client.command(aliases=["set-alarm"])
async def alarm(ctx, time):
    # Take user input (time in 24-hour format), for example 23:00
    # Check if it is a valid 24-hour format, and return an apppropriate message
    # Parse the user input using time.split(":")
    # Remind the user as soon as it's time
    pass