import discord
from discord import member
from discord import channel
from discord.ext import commands
from discord.flags import Intents

Intents = discord.Intents.default()
Intents.members = True


bot = commands.Bot(command_prefix="]",intents =Intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    print("join")
    channel = bot.get_channel(913551834889715762)
    await channel.send(f"{member}join!")

@bot.event
async def on_member_remove(member):
    print("leave")
    channel = bot.get_channel(898731444459946084)
    await channel.send(f"{member}leave!goodbye!")

bot.run("OTEzNTMzMTc0NDg1Nzc4NDYy.YZ_4EQ.e2VpSe6W4V4M4_6fJkwA0qNox3c")



