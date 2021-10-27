
from discord.ext import commands, tasks

class hourly_reminder(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["hourly-reminder", "set-hourly-reminder", "hourly-reminders", "hourly"])
  async def hourly_reminder(self, ctx,*, task):
      """
      Sets a reminder for a give task each hour.
      Args:
          ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
          task (str): The task to be reminded of
      """
      # Takes input from the user (task) about what they would like to accomplish
      await ctx.send(ctx.author.mention + f" Task: {task}, saved successfully")

      # Start reminder loop
      self.reminder_loop.start(ctx, task)

    
  @tasks.loop(minutes=0.1)
  async def reminder_loop(self, ctx, task):
      """ Send reminder to user and repeat reminder every hour unless user confirms


      """
      # Send reminder and ask for confirmation
      await ctx.send(ctx.author.mention + f" Task: \"{task}\", should be completed by the end of the hour, \nHave done it already?")

      # Check message source
      def check(m):
          return m.channel == ctx.channel and m.author == ctx.author

      # Wait for user reply to cancel loop
      # If input is not understandable, try again 2 more times
      for _i in range(3):
          try:
              reply = await self.client.wait_for("message", check=check, timeout=300)
              if reply.content.lower() in ["stop", "yes", "yep", "done", "sure" , "yeah" , "yea", "ye"]:
                  await ctx.send(ctx.author.mention + f" Congratulations, you finished your hourly task: \n\t\"{task}\"")
                  self.reminder_loop.cancel()
                  break
              elif reply.content.lower() in ["no", "nope", "not yet", "not done", "incomplete"]:
                  await ctx.send(ctx.author.mention + " Okay, I'll remind you again in another 20 minutes")
                  break
              else:
                  if _i < 2:
                      await ctx.send(ctx.author.mention + " I couldn't understand you! Type 'yes' or 'yep' if you're done, or 'no' or 'nope' if you aren't!")
                  else:
                      await ctx.send(ctx.author.mention + "I'm sorry, I couldn't understand you! I'll come back in another 20 minutes to remind you again!")
                      break

          # Continue in case of timeout
          except Exception:
              await ctx.send(ctx.author.mention + " I'll remind you again in an another 20 minutes")
              break


  @commands.command(aliases=["break_hourly","stop_hourly"])
  async def delete_hourly(self, ctx):
      #cancelling the current hourly task
      await ctx.send(ctx.author.mention + f"Task successfully deleted!")
      self.reminder_loop.cancel()

def setup(client):
  client.add_cog(hourly_reminder(client))