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
async def alarm(ctx, time):  # Take user input (time in 24-hour format), for example 23:00

    # Check if it is a valid 24-hour format, and return an apppropriate message 14:30
    
    hr=time[:2] #takes the first two indexes of the string time
    hr=int(hr) 
    if ((hr<0) or (hr>24)): #checks whether the input hour lies within 0hr to 24
        await ctx.send("Please enter valid 24 hour format time! ")
    
    mins=time[3:]
    mins=int(mins)
    if ((mins<0)or (mins>60)):   #checks whether the input minutes lies within 0 to 60mins
        await ctx.send("Please enter valid 24 hour format")
    
    t1=hr*3600
    t2=mins*60
    t=t1+t2 #converts everything into seconds
    
    from datetime import date,datetime
    userhr=datetime.datetime.now()
    uh=userhr.strftime("%H") #built-in function that will take the real time hour
    uh=int(uh)

    usermin=datetime.datetime.now()
    um=usermin.strftime("M") #built-in function that will take the real time in minutes
    um=int(um)

    usersec= (uh*3600)+(um*60)
    
    diff=t-usersec

    if(diff>0):
        {
            msg=await ctx.send(f"Alarm is set for:{time}")

            while True:
                diff -=1
                if diff==0:
                    await ctx.send(f"{ctx.msg.author.mention},Your ALARM HAS ENDED! ") # Remind the user as soon as it's time
                    break
                else:
                    await msg.edit(content=(f"Time remaining in hours:{diff/3600}")) #gives a remainder after every hour 
                    await asyncio.sleep(3600) #sleep for 1 hour,i.e. 3600 seconds

                
        }
    else:
        await ctx.send("Invalid, time cannot be counted backwards! ")
    
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
