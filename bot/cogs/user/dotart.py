from discord.ext.commands import Cog, Bot, Context
from discord.ext import commands
from discord import app_commands
from requests import get as request
from urllib.request import quote
from random import randrange
from bs4 import BeautifulSoup
from textwrap import wrap


CHARACTERS = {
    *map(chr, range(0x2800, 0x2900)), # braille
    *map(chr, range(0x2500, 0x25B0)), # blocks
    *'⚪⚫❤⬛⬜💓💔💕💖💗💘💙💚💛💜💞💟🔴🔵🖤🟠🟡🟢🟣🟤🟥🟦🟧🟨🟩🟪🟫🤍🤎🧡🩷'
}

def is_picture(art: str) -> bool:
    if art.count('\n') < 2:
        return False
    if sum(1 for c in art if c in CHARACTERS) < 25:
        return False
    return True

def get_request(query: str) -> str:
    return quote(query.replace(' ', '-'))

def get_arts(query: str) -> list[str]:
    url = f'https://emojicombos.com/{get_request(query)}'
    response = request(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all(class_='emojis')
    return list(t for d in divs if is_picture(t := d.contents[0].text))


class DotartCogs(Cog, name='Manager for emojis'):

    def __init__(self, bot: Bot):
        self.bot = bot
    
    @commands.hybrid_command(description='Sends random dot art in your chat',
                             usage='dotart <query>')
    @app_commands.describe(query='Query')
    async def dotart(self, ctx: Context, query: str) -> None:
        await ctx.defer()
        if arts := get_arts(query):
            number = randrange(len(arts))
            content = wrap(f'{arts[number]}\nArt: {number+1} / {len(arts)}',
                           width=2000,
                           replace_whitespace=False,
                           break_on_hyphens=False)
            await ctx.reply(content)
        else:
            await ctx.reply('No art found v_v')


async def setup(bot: Bot) -> None:
    await bot.add_cog(DotartCogs(bot))
