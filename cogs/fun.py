import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import urllib
import random
from random import randint
import datetime
import sqlite3
import aiohttp
import asyncio
import json
import requests


class FunCog(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.default)
    async def meme(self, ctx):
        """Gives you a random meme"""
        number = randint(0, 100)
        url = "https://www.reddit.com/r/dankmemes.json?sort=new&limit=100"
        url2 = "https://www.reddit.com/r/memeeconomy.json?sort=new&limit=100"
        url = random.choice([url, url2])
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as f:
                if f.status == 200:
                    data = (await f.json())["data"]["children"][number]["data"]
                    s=discord.Embed()
                    s.set_author(name=data["title"], url="https://www.reddit.com" + data["permalink"])
                    s.set_image(url=data["url"])
                    s.set_footer(text='Princess')
                    s.timestamp = datetime.datetime.utcnow()
                    await ctx.send(embed=s)
                else:
                    await ctx.send(await f.text())

    @commands.command()
    async def catfact(self, ctx):
        """Learn cat stuff"""
        url = "https://catfact.ninja/fact"
        request = Request(url)
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(description=data["fact"], colour=ctx.message.author.colour)
        s.set_author(name="Did you know?")
        s.set_thumbnail(url="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/134/cat-face_1f431.png")
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=s)
        
    @commands.command()
    async def dog(self, ctx):
        """Shows a random dog"""
        url = "https://dog.ceo/api/breeds/image/random"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        s=discord.Embed(description=":dog:", colour=ctx.message.author.colour)
        s.set_image(url=data["message"])
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The dog didn't make it, sorry :no_entry:")

    @commands.command()
    async def birb(self, ctx):
        url = "https://api.alexflipnote.xyz/birb"
        try:
            response = requests.get(url, timeout=2).json()
        except:
            return await ctx.send("Request timed out :no_entry:")
        s=discord.Embed(description=":bird:", colour=ctx.author.colour)
        s.set_image(url=response["file"])
        s.set_footer(text="api.alexflipnote.xyz")
        await ctx.send(embed=s)
        
    @commands.command()
    async def cat(self, ctx):
        """Shows a random cat"""
        try:
            response = requests.get("http://aws.random.cat/meow", timeout=2).json()
        except:
            return await ctx.send("Request timed out :no_entry:")
        image = response["file"]
        s=discord.Embed(description=":cat:", colour=ctx.message.author.colour)
        s.set_image(url=image)
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The cat didn't make it, sorry :no_entry:")
		
    @commands.command()
    async def kiss(self, ctx):
        "Shows a random kiss"
        #url = "https://random-d.uk/api/v1/random"
        url = "https://nekos.life/api/v2/img/kiss"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(description=f"{ctx.user.mention}",colour=ctx.message.author.colour)
        s.set_image(url=data["url"])
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The duck didn't make it, sorry :no_entry:")

    @commands.command()
    async def stare(self, ctx):
        "Shows a random stare"
        #url = "https://random-d.uk/api/v1/random"
        url = "https://rra.ram.moe/i/r?type=stare"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(colour=ctx.message.author.colour)
        s.set_image(url=data["url"])
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The duck didn't make it, sorry :no_entry:")

    @commands.command()
    async def slap(self, ctx):
        "Shows a random slap"
        #url = "https://random-d.uk/api/v1/random"
        url = "https://nekos.life/api/v2/img/slap"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(colour=ctx.message.author.colour)
        s.set_image(url=data["url"])
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The duck didn't make it, sorry :no_entry:")

    @commands.command()
    async def poke(self, ctx):
        "Shows a random poke"
        #url = "https://random-d.uk/api/v1/random"
        url = "https://nekos.life/api/v2/img/poke"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(colour=ctx.message.author.colour)
        s.set_image(url=data["url"])
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The duck didn't make it, sorry :no_entry:")


    @commands.command()
    async def nom(self, ctx):
        "Shows a random nom"
        #url = "https://random-d.uk/api/v1/random"
        url = "https://rra.ram.moe/i/r?type=nom"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(colour=ctx.message.author.colour)
        s.set_image(url=data["url"])
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The duck didn't make it, sorry :no_entry:")

    @commands.command()
    async def hug(self, ctx):
        "Shows a random hug"
        #url = "https://random-d.uk/api/v1/random"
        url = "https://nekos.life/api/v2/img/hug"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(colour=ctx.message.author.colour)
        s.set_image(url=data["url"])
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The duck didn't make it, sorry :no_entry:")

    @commands.command()
    async def cuddle(self, ctx):
        "Shows a random cuddle"
        #url = "https://random-d.uk/api/v1/random"
        url = "https://nekos.life/api/v2/img/cuddle"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(colour=ctx.message.author.colour)
        s.set_image(url=data["url"])
        s.set_footer(text='Princess')
        s.timestamp = datetime.datetime.utcnow()
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The duck didn't make it, sorry :no_entry:")

    @commands.command()
    async def fox(self, ctx):
        "Shows a random fox"
        url = "https://randomfox.ca/floof/"
        request = Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        data = json.loads(urlopen(request).read().decode())
        s=discord.Embed(description=":fox:", colour=ctx.message.author.colour)
        s.set_image(url=data["image"])
        try:
            await ctx.send(embed=s)
        except:
            await ctx.send("The Fox didn't make it, sorry :no_entry:")
   


def setup(bot):
    bot.add_cog(FunCog(bot))   
    print('Automod on raedy') 
