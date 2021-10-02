import discord
from discord.ext import commands
import asyncio
import time

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")


from stopwatch import stopwach
from pomodoro import pomodoro
from daily_remainder import daily_reminder
from hourly_reminder import hourly_reminder
from alarm import alarm
from timer import start_timer


@client.event
async def on_ready():
    print("Bot is ready")





def getQuote(tags=["education", "success"]):  # default arguments
    # Fetch quotes using an API
    # https://github.com/lukePeavey/quotable
    pass


client.run(config["token"])
