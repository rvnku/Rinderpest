from discord.ext.commands import Cog, Bot, Context
from discord.ext import commands


class ModCog(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.hybrid_command()
    async def clear(self, ctx: Context, *,
                         count: int = commands.parameter(description='Count of messages')):
        """Clear latest messages"""

        await ctx.defer()

        messages = [message async for message in ctx.channel.history(limit=int(count))]
        await ctx.channel.delete_messages(messages)
        reply = await ctx.reply('Messages successfully deleted!')
        await reply.delete(5.0)


async def setup(bot: Bot) -> None:
    await bot.add_cog(ModCog(bot))
