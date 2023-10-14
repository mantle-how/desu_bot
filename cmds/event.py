#!/usr/bin/python3
#此類存放觸發類型code
import discord

from discord.ext import commands
from cores.cog_extention import cog_extension

import json

with open('setting.json', 'r',encoding='utf-8')as jfile:
    jdata = json.load(jfile)

class event(cog_extension):
    @commands.Cog.listener() #從bot.event變成commands.Cog.listener()
    #on_member_join為discord.py內部已經定義的函式
    #而括號內的變數內部也已經定義為member不得修改。而且member只能一個
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata["join_channel"]))
   
        await channel.send(f'{member}已加入')

    @commands.Cog.listener() #從bot.event變成commands.Cog.listener()
    #on_member_remove為discord.py內部已經定義的函式，而member定義同join
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata["leave_channel"]))
        
        await channel.send(f'{member}已離開')
    @commands.Cog.listener()
    async def on_message(self,ctx):
        #send內只能用單引號字串

        if ctx.content in (jdata["keyword1"]) and ctx.author != self.bot.user:#auther 為傳出訊息者
            await ctx.channel.send('pie')
        elif ctx.content in (jdata["keyword2"]) and ctx.author != self.bot.user:
            await ctx.channel.send('soup')
        elif ctx.content.endswith("gun")and ctx.author != self.bot.user:
            await ctx.channel.send('they are all gun')
    

    
async def setup(bot):
    await bot.add_cog(event(bot))
