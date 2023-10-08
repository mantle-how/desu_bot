#!/usr/bin/python3
import discord

from discord.ext import commands

import json

import random
import os
import asyncio

with open('setting.json','r',encoding="utf-8")as jfile:
    jdata = json.load(jfile)
    

#intents為discord.py ver1.5更新後強制使用的功能選擇功能
intents = discord.Intents.all() 

#在ver1.5之後需要再宣告機器人為client或bot的這段後面加上intents = intents
bot = commands.Bot(command_prefix='%', intents = intents)

@bot.event
#on_ready()為discord.py內部已經定義的函式
async def on_ready():
    print("bot is working")

@bot.event
#on_member_join為discord.py內部已經定義的函式
#而括號內的變數內部也已經定義為member不得修改。而且member只能一個
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["join_channel"]))
   
    await channel.send(f'{member}已加入')

@bot.event 
#on_member_remove為discord.py內部已經定義的函式，而member定義同join
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["leave_channel"]))
    
    await channel.send(f'{member}已離開')


@bot.command()
async def load(ctx,extension):
    await bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"loaded {extension} done")

@bot.command()
async def unload(ctx,extension):
    await bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"unloaded {extension} done")

@bot.command()
async def reload(ctx,extension):
    await bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"reloaded {extension} done")




async def loadfile():
    for filename in os.listdir("./cmds"):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

   
#啟動函式
if __name__=="__main__":
    asyncio.run(loadfile())





    

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])

