import discord
from discord.ext import commands
import asyncio

class timer(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["timer", "start-timer"])
  async def start_timer(self, ctx, seconds):
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


def setup(client):
  client.add_cog(timer(client))