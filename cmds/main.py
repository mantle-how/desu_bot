#!/usr/bin/python3
#此為功能性指令
import discord

from discord.ext import commands

from cores.cog_extention import cog_extension
import json

class main(cog_extension):
    @commands.command() #從bot.command變成commands.command
    #command 中的def幾乎都為prefix後接的指令

    # 在ping()中的變數為ctx，ctx全名為context(上下文)，上文為開頭，下文為回覆
    # 而在ctx中上文已經有包含所在伺服器 使用者等等資訊 


    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')
    
    @commands.command()
    #msg argument會將使用者傳出的訊息這則資料傳到這則變數中，因為ctx.message會報error所以需要用這方法。
    async def sayd(self,ctx,*,msg):#在argument前加*代表後面的所有資料傳入*後的argument
        await ctx.message.delete()
        await ctx.send(msg)
        
    @commands.command()
    async def clear(self, ctx, num:int):
        await ctx.channel.purge(limit = num+1)

async def setup(bot):
    await bot.add_cog(main(bot))
