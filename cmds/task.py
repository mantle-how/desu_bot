#!/usr/bin/python3
import discord
from discord.ext import commands
from cores.cog_extention import cog_extension
import json, asyncio, datetime
from discord.ext import tasks
class task(cog_extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_background_task.start()
        self.my_background_task_running = True  # 初始狀態為執行
        async def unload_cog(self):
            await self.my_background_task.stop()
        
    @commands.command()
    async def task_start(self, ctx):
        if not self.my_background_task_running:
            self.my_background_task_running = True
            self.my_background_task.start()
            await ctx.send("Started the background task.")
        else:
            await ctx.send("The background task is already running.")

    @commands.command()
    async def task_stop(self, ctx):
        if self.my_background_task_running:
            self.my_background_task_running = False
            self.my_background_task.stop()
            await ctx.send("Stopped the background task.")
        else:
            await ctx.send("The background task is not running.")



    





    @tasks.loop(seconds=5)
    async def my_background_task(self):
        await self.bot.wait_until_ready()
            
            
        # 設定發送訊息的頻道ID
        channel_id = 1153325428380024925
        channel = self.bot.get_channel(channel_id)
            
            

        await channel.send("🛏 晚安！瑪卡巴卡！")
        print("yap")
    
 
            
        
        

      

async def setup(bot):
    await bot.add_cog(task(bot))
