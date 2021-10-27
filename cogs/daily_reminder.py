
from discord.ext import commands, tasks

class daily_reminder(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["daily-reminder", "set-daily-alarm" , "daily"])
  async def daily_reminder(self, ctx,*, task):
      """
      Sets a reminder for a give task each day.
      Args:
          ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
          task (str): The task to be reminded of
      """
      # Takes input from the user (task) about what they would like to accomplish
      await ctx.send(ctx.author.mention + f" Task: {task}, saved successfully")

      # Start reminder loop
      self.reminder_loop.start(ctx, task)


  @tasks.loop(minutes=60)
  async def reminder_loop(self, ctx, task):
      """ Send reminder to user and repeat reminder every hour unless user confirms

      Args:
          ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
          task (str): The task to be reminded of

      """
      # Send reminder and ask for confirmation
      await ctx.send(ctx.author.mention + f" Task: \"{task}\", should be completed today, \nHave done it already?")

      # Check message source
      def check(m):
          return m.channel == ctx.channel and m.author == ctx.author

      # Wait for user reply to cancel loop
      # If input is not understandable, try again 2 more times
      for _i in range(3):
          try:
              reply = await self.client.wait_for("message", check=check, timeout=300)
              if reply.content.lower() in ["stop", "yes", "yep", "done", "sure"]:
                  await ctx.send(ctx.author.mention + f" Congratulations, you finished your daily task: \n\t\"{task}\"")
                  self.reminder_loop.cancel()
                  break
              elif reply.content.lower() in ["no", "nope", "not yet", "not done", "incomplete"]:
                  await ctx.send(ctx.author.mention + " Okay, I'll remind you again in an hour")
                  break
              else:
                  if _i < 2:
                      await ctx.send(ctx.author.mention + " I couldn't understand you! Type 'yes' or 'yep' if you're done, or 'no' or 'nope' if you aren't!")
                  else:
                      await ctx.send(ctx.author.mention + "I'm sorry, I couldn't understand you! I'll come back in an hour to remind you again!")
                      break

          # Continue in case of timeout
          except Exception:
              await ctx.send(ctx.author.mention + " I'll remind you again in an hour")
              break


  @commands.command(aliases=["break_daily","stop_daily"])
  async def delete_daily(self, ctx):
      #cancelling the current daily task
      await ctx.send(ctx.author.mention + f"Task successfully deleted!")
      self.reminder_loop.cancel()

def setup(client):
  client.add_cog(daily_reminder(client))