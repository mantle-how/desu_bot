#!/usr/bin/python3
import discord

from discord.ext import commands


class cog_extension(commands.Cog): #.Cog的C一定要為大寫
    def __init__(self,bot):
        self.bot = bot
        

