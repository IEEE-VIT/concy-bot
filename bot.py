import discord
from discord.ext import commands, tasks
import asyncio
import aiohttp
import json

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=commands.when_mentioned_or("."))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 


@client.command(aliases=["timer", "start-timer"])
async def start_timer(ctx, seconds):
    """Starts a timer for a given number of seconds
    Args:
        ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
        seconds (time): The number of seconds to set the timer to.
    """
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
    """Sets an alarm for a given time
    Args:
        ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
        time ([type]): time in 24 hour format
    """
    # Take user input (time in 24-hour format), for example 23:00
    # Check if it is a valid 24-hour format, and return an apppropriate message
    # Parse the user input using time.split(":")
    # Remind the user as soon as it's time
    pass


@client.command(aliases=["stopwatch", "start-stopwatch"])
async def stopwach(ctx):
    """Starts a stopwatch until the user types 'stop'
    Args:
        ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
    """
    # Start a stopwatch
    # Wait for the stop command from user (You may use "client.wait_for")
    pass


@client.command(aliases=["hourly-reminder", "set-hourly-reminder"])
async def hourly_reminder(ctx, task):
    """Sets a reminder for a give task each hour
    Args:
        ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
        task (str): The task to be reminded of
    """
    # Takes input from the user (task) about what they would like to accomplish
    # Send a reminder after one hour to see how far they have come up with the task
    # At the end of every hour, ask the user if they have completed the task.
    # Wait for the stop command from user (You may use "client.wait_for")
    pass


@client.command(aliases=["daily-reminder", "set-daily-alarm"])
async def daily_reminder(ctx,*, task):
    """
    Sets a reminder for a give task each day.
    Args:
        ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
        task (str): The task to be reminded of
    """
    # Takes input from the user (task) about what they would like to accomplish
    await ctx.send(ctx.author.mention + f" Task: {task}, saved successfully")

    # Start reminder loop
    reminder_loop.start(ctx, task)


@tasks.loop(minutes=60)
async def reminder_loop(ctx, task):
    """ Send reminder to user and repeat reminder every hour unless user confirms

    Args:
        ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
        task (str): The task to be reminded of

    """
    # Send reminder and ask for confirmation
    await ctx.send(ctx.author.mention + f" Task: \"{task}\", should be completed today, \nHave done it already?")

    # Check message source
    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author

    # Wait for user reply to cancel loop
    # If input is not understandable, try again 2 more times
    for _i in range(3):
        try:
            reply = await client.wait_for("message", check=check, timeout=300)
            if reply.content.lower() in ["stop", "yes", "yep", "done", "sure"]:
                await ctx.send(ctx.author.mention + f" Congratulations, you finished your daily task: \n\t\"{task}\"")
                reminder_loop.cancel()
                break
            elif reply.content.lower() in ["no", "nope", "not yet", "not done", "incomplete"]:
                await ctx.send(ctx.author.mention + " Okay, I'll remind you again in an hour")
                break
            else:
                if _i < 2:
                    await ctx.send(ctx.author.mention + " I couldn't understand you! Type 'yes' or 'yep' if you're done, or 'no' or 'nope' if you aren't!")
                else:
                    await ctx.send(ctx.author.mention + "I'm sorry, I couldn't understand you! I'll come back in an hour to remind you again!")
                    break

        # Continue in case of timeout
        except Exception:
            await ctx.send(ctx.author.mention + " I'll remind you again in an hour")
            break


@client.command(aliases=["break_daily","stop_daily"])
async def delete_daily(ctx):
    #cancelling the current daily task
    await ctx.send(ctx.author.mention + f"Task successfully deleted!")
    reminder_loop.cancel()


@client.command(aliases=["start-pomodoro"])
async def pomodoro(ctx):
    """Starts a pomodoro timer for 25 minutes
    ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
    """
    # Set a timer for 25 minutes
    time = 1500
    # Notify the user after 25 minutes
    message = await ctx.send("Your countdown has been started for 25 minutes")
    while True:
        time -= 1
        if time == 0:
            await ctx.send(ctx.message.author.mention + " your break has started.")
            break

        await asyncio.sleep(1)
    # Set the timer for 5 minutes (starting of the break)
    time = 300
    await message.edit(content=("Your break countdown has been started for 5 minutes"))
    while True:
        time -= 1
        if time == 0:
            break

        await asyncio.sleep(1)
    # Notify the user after 5 minutes that Pomodoro has ended
    await ctx.send(ctx.message.author.mention + " Pomodoro has ended!")

@client.command(aliases=["quote","motivation"])
async def motivational_quote(ctx, message = " "):
    """ Get a random quote from the API based on the tags provided
    Args:
        ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
        tags (list, optional): Tags provided by the user. Defaults to ["inspirational", "success"].
        tags (list, optional): Tags provided by the user.
    """
    # tags that are available in the quoteable api
    user = message.lower()
    if user == "daily":
        async with aiohttp.ClientSession() as session:
            async with session.get("https://zenquotes.io/api/today") as response:
                json_data = json.loads(await response.text())
                quote = json_data[0]["q"] + " - " + json_data[0]['a']
                await ctx.send(quote)
    elif user == " ":   
        async with aiohttp.ClientSession() as session:
            async with session.get("https://zenquotes.io/api/random") as response:
                json_data = json.loads(await response.text())
                quote = json_data[0]["q"] + " - " + json_data[0]['a']
                await ctx.send(quote)
    else:
        await ctx.send(f"{ctx.author.mention} Please make sure if you have no spelling error in the command")

client.run(config["token"])
