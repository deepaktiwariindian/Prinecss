import discord
from discord.ext import commands
import datetime
import sqlite3

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx, *cog):

        if not cog:

            embed = discord.Embed(title="Princess Help Menu", description='''These are the available commands for Princess's Palace
                                The bot's prefix is: {ctx.prefix}
                                Command Parameters: <> is strict & [] is optional''',
                                color=0xFF00FF)
            cogs_desc = ''
            for x in self.bot.cogs:
                cogs_desc += ('**{}** - {}'.format(x,self.bot.cogs[x].__doc__)+'\n')
            embed.add_field(name='Cogs',value=cogs_desc[0:len(cogs_desc)-1],inline=False)
            embed.add_field(name="Prinecss", value="[Invite](https://discord.com/oauth2/authorize?scope=bot&permissions=2146958847&client_id=479143648668155905) | [Support server](https://discord.gg/7awJQNu) | [PayPal](https://www.paypal.me/drbossop) | [Vote](https://top.gg/bot/479143648668155905/vote)")
            embed.set_footer(text="*help <command/module> for more info", icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.message.add_reaction(emoji='✉')
        else:
            if len(cog) > 1:
                embed = discord.Embed(title='Error!',description='That is way too many cogs!',color=discord.Color.red())
                await ctx.message.author.send('',embed=embed)
            else:
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            embed = discord.Embed(title='Error!',color=0xFF00FF)
                            scog_info = ''
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    scog_info += f'**{c.name}** - {c.help}\n'
                            embed.add_field(name=f'{cog[0]} - {self.bot.cogs[cog[0]].__doc__}', value=scog_info)
                            found = True
                if not found:
                    for x in self.bot.cogs:
                        for c in self.bot.get_cog(x).get_commands(): 

                            if c.name == cog[0]:
                                embed = discord.Embed(title=f'Command: {c.name}',color=0xFF00FF)
                                embed.add_field(name=f'Description: {c.help}', value=f'Usage: `{c.qualified_name} {c.signature}`')

                        found = True
                    if not found:
                        embed = discord.Embed(title='Error!',description='How do you even use "'+cog[0]+'"?',color=discord.Color.red())
                else:
                    await ctx.message.add_reaction(emoji='✉')
                await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(HelpCog(bot))
    print('Help on raedy')
