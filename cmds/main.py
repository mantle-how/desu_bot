#!/usr/bin/python3
import discord

from discord.ext import commands

from cores.cog_extention import cog_extension

class main(cog_extension):
    @commands.command()
    #command 中的def幾乎都為prefix後接的指令

    # 在ping()中的變數為ctx，ctx全名為context(上下文)，上文為開頭，下文為回覆
    # 而在ctx中上文已經有包含所在伺服器 使用者等等資訊


    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

async def setup(bot):
    await bot.add_cog(main(bot))
