import discord
from discord.ext import commands

class alarm(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["set-alarm"])
    async def alarm(self, ctx, time):
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

def setup(client):
    client.add_cog(alarm(client))