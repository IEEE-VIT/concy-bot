import discord
from discord.ext import commands, tasks

class hourly_reminder(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["hourly-reminder","set-hourly-reminder"])
    async def hourly_reminder(self, ctx, task):
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

def setup(client):
    client.add_cog(hourly_reminder(client))