import discord
from discord.ext import commands
import asyncio
import time

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")

@client.command(aliases=["daily-reminder", "set-daily-alarm"])
async def daily_reminder(ctx, time):
    # Takes input from the user (task) about what they would like to accomplish
    # Send a reminder after 24 hours to see how far they have come up with the task
    # At the end of every hour, ask the user if they have completed the task.
    # Wait for the stop command from user (You may use "client.wait_for")
    pass