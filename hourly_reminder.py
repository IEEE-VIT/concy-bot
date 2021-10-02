import discord
from discord.ext import commands
import asyncio
import time

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")


@client.command(aliases=["hourly-reminder", "set-hourly-reminder"])
async def hourly_reminder(ctx, task):
    # Takes input from the user (task) about what they would like to accomplish
    # Send a reminder after one hour to see how far they have come up with the task
    # At the end of every hour, ask the user if they have completed the task.
    # Wait for the stop command from user (You may use "client.wait_for")
    pass
