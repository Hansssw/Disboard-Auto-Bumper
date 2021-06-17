import discord, os, time
from discord.ext import commands # https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html

# More improvements example: https://codeberg.org/SnowCode/auto-bump


# Uncomment the line below if you are wanting to host this on heroku and are using an environment variable to store the token.
token = os.getenv("USER_TOKEN")
# If you are using this on a server or your home pc uncomment the line below and put the discord token for the account you want it to auto bump on.
#token = "TOKEN"

botReceive = commands.Bot(command_prefix = "--", self_bot=True) # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=run#bot

@botReceive.event
async def on_ready():
    print("Auto Bumper Is Online!") 
    print("Auto Bumper " + str(botReceive.user)) # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=run#discord.ext.commands.Bot.user

@botReceive.command()
async def bla(ctx): # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Context
    while True:
        await ctx.send("!d bump")
        await ctx.send(ctx.author)
        print("Auto Bumper bla command has been done in #" + str(ctx.channel) + " by " + str(ctx.author))
        time.sleep(10) # 8125 seconds == 2 hours



botReceive.run(token, bot = False)
















@bot.event
async def on_connect():
    print("Auto Bumper successfully connected to Discord!")


    
@bot.event
async def on_disconnect():
    print("Auto Bumper: Discord.com is down or the Bot can not connect to the internet")
