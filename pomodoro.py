import discord
from discord.ext import commands
import asyncio
import time

from dotenv import dotenv_values

config = dotenv_values(".env")
client = commands.Bot(command_prefix=".")


@client.command(aliases=["start-pomodoro"])
async def pomodoro(ctx, time):
    print("Pomodoro starts now!")
    for i in range(4):
        t=25*60
        while t:
            mins = t // 60
            secs = t%60
            timer = '{:02d}:{:02d}'.format(mins,secs)
            print(timer, end="\r")
            time.sleep(1)
            t -=1
            print("Break time!!")
            t= 5*60
            while t:
                mins = t//60
                secs = t%60
                timer= '{:02d}:{:02d}'.format(mins,secs)
                print(timer, end="\r")
                time.sleep(1)
                t -=1
                print("Work time!!")

   
    pass