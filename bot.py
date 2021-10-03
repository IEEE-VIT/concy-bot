import discord
from discord.ext import commands, tasks
import asyncio
import urllib.request
import json

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("Bot is ready")


@client.command(aliases=["timer", "start-timer"])
async def start_timer(ctx, seconds):
    """Starts a timer for a given number of seconds

    Args:
        ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
        seconds (time): The number of seconds to set the timer to.
    """
    if not seconds.isnumeric():
        print("Not a number")
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
async def daily_reminder(ctx, task):
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
    # Send reminder and ask for confirmation
    await ctx.send(
        ctx.author.mention
        + f' Task: "{task}", should be completed today, \nHave done it already?'
    )

    # Check message source
    def check(m):
        return m.channel == ctx.channel and m.author == ctx.author

    # Wait for user reply to cancel loop
    try:
        reply = await client.wait_for("message", check=check, timeout=300)
        if reply.content.lower() in ["stop", "yes", "yep", "done", "sure"]:
            await ctx.send(
                ctx.author.mention
                + f' Congratulations, you finished your daily task: \n\t"{task}"'
            )
            reminder_loop.cancel()
        else:
            await ctx.send(
                ctx.author.mention + " Okay, I'll remind you again in an hour"
            )

    # Continue in case of timeout
    except Exception:
        await ctx.send(ctx.author.mention + " I'll remind you again in an hour")


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


def getQuote(tags=["inspirational", "success"]):  # default arguments
    """Get random quote from the API

    Args:
        tags (list, optional): [description]. Defaults to ["inspirational", "success"].
    """
    # add tags to the url
    url = "https://api.quotable.io/random?tags="
    for tag in tags:
        url = url + tag + "|"
    # get json response from the quoteable api
    response = urllib.request.urlopen(url).read()
    # Convert json response into a dictionary
    response_dict = json.loads(response)
    quote_author = response_dict["author"]
    quote_text = response_dict["content"]

    return (quote_text, quote_author)


@client.command(aliases=["quote", "motivation"])
async def motivational_quote(ctx, *tags):
    # tags that are available in the quoteable api
    AVAILABLE_TAGS = [
        "business",
        "education",
        "faith",
        "famous-quotes",
        "friendship",
        "future",
        "happiness",
        "history",
        "inspirational",
        "life",
        "literature",
        "love",
        "nature",
        "politics",
        "proverb",
        "religion",
        "science",
        "success",
        "technology",
        "wisdom",
    ]
    # check if the tags enterend as arguments are valid
    quote = ()
    if len(tags) > 0:
        if set(tags).issubset(set(AVAILABLE_TAGS)):
            quote = getQuote(tags=tags)
        else:
            await ctx.send(
                "Invalid tag\nthe available tags are:\n" + ", ".join(AVAILABLE_TAGS)
            )
            return
    else:
        quote = getQuote()
    quote_text = '"' + quote[0] + '"'
    quote_author = "-" + quote[1]
    # Make a discord embed with quote
    quote_embed = discord.Embed(
        title="Motivational Quote",
        description=quote_text,
    )
    quote_embed.set_footer(text=quote_author)
    await ctx.send(embed=quote_embed)


client.run(config["token"])
