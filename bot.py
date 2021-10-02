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



    
    

@client.command(aliases=["hourly-reminder", "set-hourly-reminder"])
async def hourly_reminder(ctx, task): # Takes input from the user (task) about what they would like to accomplish

    
    await ctx.send(f"YOU HAVE TO COMPLETE {task} and once you have done, write *stop ") #Sends a reminder after one hour to see how far they have come up with the task

    # This will make sure that the response will only be registered if the following
    # conditions are met:
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
        msg.content.lower() in ["stop"] # Wait for the stop command from user (You may use "client.wait_for")

    msg = await client.wait_for("message", check=check)
    
    
    while(msg.content.lower() != "stop"):
           await ctx.send(f"One hour is over PLEASE COMPLETE YOUR {task} SOON")
           await asyncio.sleep(3600) # At the end of every hour, ask the user if they have completed the task.
    await ctx.send(f"CONGRATULATIONS YOU HAVE COMPLETED YOUR {task}")  
    
    pass



    
    
    
    
  


@client.command(aliases=["daily-reminder", "set-daily-alarm"])
async def daily_reminder(ctx, task):  # Takes input from the user (task) about what they would like to accomplish
    
    
    
    # Send a reminder after 24 hours to see how far they have come up with the task
    # At the end of every hour, ask the user if they have completed the task.
    # Wait for the stop command from user (You may use "client.wait_for")
    pass


@client.command(aliases=["start-pomodoro"])
async def pomodoro(ctx, time):
    # Set a timer for 25 minutes
    # Notify the user after 25 minutes
    # Set the timer for 5 minutes (starting of the break)
    # Notify the user after 5 minutes that Pomodoro has ended
    pass


def getQuote(tags=["education", "success"]):  # default arguments
    # Fetch quotes using an API
    # https://github.com/lukePeavey/quotable
    pass


client.run(config["token"])
