import discord
import asyncio
from discord.ext import commands, tasks

class stopwatch(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["stopwatch", "start-stopwatch"])
    async def stopwach(self, ctx):
        """
        Start a stopwatch on command, which stops after user command and shows total elapsed time in seconds.

        Args:
            ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
        """
        second = 0
        await ctx.send("Your stopwatch has been started...Send 'stop', to stop the watch.")
        message = await ctx.send((f"Time elapsed : {second} second(s)"))

        while True :
            second += 1

            await message.edit(content=(f"Time elapsed : {second} second(s)"))
            try: 
                await self.client.wait_for("message", check= lambda x: x.author == ctx.author and "stop" in x.content, timeout=1)
            except asyncio.TimeoutError:
                continue
            else:
                await ctx.send(content=(f"Total time elapsed : {str(second)} second(s)"))
                break

def setup(client):
    client.add_cog(stopwatch(client))

