from discord.ext import commands
import asyncio
import datetime
import time

ALLOWED_TIME_FORMAT = "%H:%M"


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
        # Check if it is a valid 24-hour format, and return an apppropriate
        # message

        try:
            alarm_time = datetime.datetime.strptime(time, ALLOWED_TIME_FORMAT)
        except ValueError:
            await ctx.send(
                ctx.message.author.mention
                + " Please input the alarm time in 24-hour format (e.g. 14:00)"
            )

        while True:
            now = datetime.now()
            if now >= alarm_time:
                await ctx.send(
                    ctx.message.author.mention
                    + f" Ding dong, it is {alarm_time}, your alarm went off!"
                )
                break
            await asyncio.sleep(1)


def setup(client):
    client.add_cog(alarm(client))
