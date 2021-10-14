import discord
from discord.ext import commands
import urllib.request
import json
import asyncio

class others(commands.Cog):

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

  def getQuote(self, tags=["inspirational", "success"]):  # default arguments
      """Get random quote from the API
      Args:
          tags (list, optional): Tags provided by the user. Defaults to ["inspirational", "success"].
      """
      #add tags to the url
      url = "https://api.quotable.io/random?tags="
      for tag in tags:
          url = url+tag+"|"
      # get json response from the quoteable api
      response = urllib.request.urlopen(url).read()
      # Convert json response into a dictionary
      response_dict = json.loads(response)
      quote_author =  response_dict["author"]
      quote_text = response_dict["content"]

      return (quote_text,quote_author)


  @commands.command(aliases=["quote","motivation"])
  async def motivational_quote(self, ctx,*tags):
      """ Get a random quote from the API based on the tags provided
      Args:
          ctx (discord.ext.commands.Context): Represents the context in which a command is being invoked under.
          tags (list, optional): Tags provided by the user. Defaults to ["inspirational", "success"].
      """
      # tags that are available in the quoteable api
      AVAILABLE_TAGS = ['business', 'education', 'faith', 'famous-quotes', 'friendship', 'future', 'happiness',
                        'history', 'inspirational', 'life', 'literature', 'love', 'nature', 'politics', 'proverb',
                        'religion', 'science', 'success', 'technology', 'wisdom']
      # check if the tags enterend as arguments are valid
      quote = ()
      if len(tags) > 0:
          if set(tags).issubset(set(AVAILABLE_TAGS)):
              quote = self.getQuote(tags=tags)
          else:
              await ctx.send("Invalid tag\nthe available tags are:\n"+", ".join(AVAILABLE_TAGS))
              return
      else:
          quote = self.getQuote()
      quote_text = "\"" + quote[0] + "\""
      quote_author = "-" + quote[1]
      # Make a discord embed with quote
      quote_embed = discord.Embed(title="Motivational Quote",description=quote_text,)
      quote_embed.set_footer(text=quote_author)
      await ctx.send(embed=quote_embed)


def setup(client):
    client.add_cog(others(client))
