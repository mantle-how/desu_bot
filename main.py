#!/usr/bin/python3
import discord

from discord.ext import commands

import json

import random

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
#command 中的def幾乎都為prefix後接的指令

# 在ping()中的變數為ctx，ctx全名為context(上下文)，上文為開頭，下文為回覆
# 而在ctx中上文已經有包含所在伺服器 使用者等等資訊


async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def pic(ctx):
    random_pic = random.choice(jdata["picture"])
    picdata = discord.File(random_pic)
    
    await ctx.send(file= picdata)
    





bot.run(jdata["TOKEN"])

