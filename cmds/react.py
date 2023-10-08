#!/usr/bin/python3
import discord

from discord.ext import commands

from cores.cog_extention import cog_extension

import random

import json
with open('setting.json','r',encoding="utf-8")as jfile:
    jdata = json.load(jfile)

class react(cog_extension):
    @commands.command()
    async def pic(self,ctx):
        random_pic = random.choice(jdata["picture"])
        picdata = discord.File(random_pic)
    
        await ctx.send(file= picdata)
    @commands.command()
    async def hi(self, ctx):
        await ctx.send("ABCD")
async def setup(bot):
    await bot.add_cog(react(bot))
