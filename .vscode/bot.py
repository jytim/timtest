import discord
from discord import member
from discord import channel
from discord.ext import commands
from discord.flags import Intents

import json
with open("setting.json",mode="r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

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

#bot離開

@bot.event
async def on_member_remove(member):
    print("leave")
    channel = bot.get_channel(898731444459946084)
    await channel.send(f"{member}leave!goodbye!")


#ctx 所在的頻道 使用者....
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}ms")

time = 0

@bot.command()
async def hi(ctx):
    global time

    if time < 10:
        await ctx.send("HELLO my friend")
        time = time +1

    if time == 5:
            await ctx.send("Please be quiet")

    if time == 10:
        await ctx.send("SHUUUUUUT UPPPP!!")
        time = 0

bot.run(jdata["TOKEN"])