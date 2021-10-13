import discord
from discord.ext import commands
import asyncio

class timers(commands.Cog):

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
  client.add_cog(timers(client))