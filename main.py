  
import discord
from discord.ext import commands
import datetime
from discord.utils import get
import sqlite3


import sys

# conn = sqlite3.connect('voice.db')
# c = conn.cursor()
# # c.execute('''CREATE TABLE IF NOT EXISTS users
# #         (roles text, server text, location text,
# #         id text, names text, postcount int, retard int, sicklad int)''')

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['*']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '*'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)



initial_extensions = ['cogs.welcome',
                      'cogs.fun',
                      'cogs.general',
                      'cogs.help']

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')
bot.remove_command("help")


# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

#on_Ready
@bot.event
async def on_ready():
    print('Online')
    print('Logged in as')
    
    
#token
bot.run('NTM4NzExNjg2MDEwNTAzMTY4.XExgWg.tfRwTY9awCELn3kivQSOeED9Sk8')
