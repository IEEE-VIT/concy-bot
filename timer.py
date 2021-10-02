import discord
from discord.ext import commands
import asyncio
import time

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")


@client.command(aliases=["timer", "start-timer"])
async def start_timer(ctx, seconds):

    if not seconds.isnumeric():
        await ctx.send("Must be a number!")

    # Convert string (user input command) into an integer
    seconds = int(seconds)
    if seconds <= 0:
        await ctx.send("I don't think I'm allowed to do negatives")

    # Send a message to the Discord channel
    await ctx.send(f"Your countdown has been started for {str(seconds)} seconds")

    # We are making a variable, so that we can reference our message later on
    # and thus, edit our message on the Discord Server
    message = await ctx.send(f"Time Remaining : {str(seconds)} second(s)")

    while True:
        seconds -= 1
        if seconds == 0:
            await message.edit(content=(f"Time Remaining : 0"))

            # Notify the author (user who issued the command) using ctx.message.author.mention
            await ctx.send(ctx.message.author.mention + " Your countdown has ended!")
            break

        # Thus, we edit our message on the Discord channel with the current remaining time
        await message.edit(content=(f"Time Remaining : {str(seconds)} second(s)"))

        # Sleep for 1 second
        await asyncio.sleep(1)