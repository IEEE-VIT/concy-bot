import discord
from discord.ext import commands
import asyncio

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready")


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


@client.command(aliases=["set-alarm"])
async def alarm(ctx, time):
    # Take user input (time in 24-hour format), for example 23:00
    # Check if it is a valid 24-hour format, and return an apppropriate message
    # Parse the user input using time.split(":")
    # Remind the user as soon as it's time
    pass


@client.command(aliases=["stopwatch", "start-stopwatch"])
async def stopwach(ctx):
    # Start a stopwatch
    # Wait for the stop command from user (You may use "client.wait_for")
    pass


@client.command(aliases=["hourly-reminder", "set-hourly-reminder"])
async def hourly_reminder(ctx, task):
    # Takes input from the user (task) about what they would like to accomplish
    # Send a reminder after one hour to see how far they have come up with the task
    # At the end of every hour, ask the user if they have completed the task.
    # Wait for the stop command from user (You may use "client.wait_for")
    pass


@client.command(aliases=["daily-reminder", "set-daily-alarm"])
async def daily_reminder(ctx, time):
    # Takes input from the user (task) about what they would like to accomplish
    # Send a reminder after 24 hours to see how far they have come up with the task
    # At the end of every hour, ask the user if they have completed the task.
    # Wait for the stop command from user (You may use "client.wait_for")
    pass


@client.command(aliases=["start-pomodoro"])
async def pomodoro(ctx, time):
    # Set a timer for 25 minutes
    time = 1500
    # Notify the user after 25 minutes
    message = await ctx.send("Your countdown has been started for 25 minutes")
    while True:
        time -= 1
        if time == 0:
            await message.edit(content=("Time remaining {:02d}:{:02d}".format(0, 0)))
            await ctx.send(ctx.message.author.mention + " your countdown has ended!\nBreak starts.")
            break

        await asyncio.sleep(1)
    # Set the timer for 5 minutes (starting of the break)
    time = 300
    await message.edit(content=("Your break countdown has been started for 5 minutes"))
    while True:
        time -= 1
        if time == 0:
            await message.edit(content=("Time remaining {:02d}:{:02d}".format(0, 0)))
            await ctx.send(ctx.message.author.mention + " your break countdown has ended!")
            break

        await asyncio.sleep(1)
    # Notify the user after 5 minutes that Pomodoro has ended
    await ctx.send(ctx.message.author.mention + " Pomodoro has ended!")

def getQuote(tags=["education", "success"]):  # default arguments
    # Fetch quotes using an API
    # https://github.com/lukePeavey/quotable
    pass


client.run(config["token"])
