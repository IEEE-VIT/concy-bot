import discord
import asyncio
from discord.ext import commands

class pomodoro(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["start-pomodoro"])
    async def pomodoro(self, ctx):
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

def setup(client):
    client.add_cog(pomodoro(client))