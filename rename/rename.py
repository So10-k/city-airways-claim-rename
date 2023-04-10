import discord
from discord.ext import commands
from core import checks

class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.thread_only()

    @commands.command()
    async def rename(self, ctx, *, request):
        try:
            embed = discord.Embed(
                title = 'Changing channel name..',
                description = ('Updating channel name to %s' % request),
                color = discord.Color.yellow()
            )
            embed.set_footer(text = 'Nicklaus#5688 • Rename')

            edit = await ctx.reply(embed = embed)
            await ctx.message.add_reaction('⏱️')

            await ctx.channel.edit(name = request) # Edit channel name, finally.

            embed = discord.Embed(
                title = 'Changed channel name!',
                description = ('Updated channel name to %s' % request),
                color = discord.Color.green()
            )
            embed.set_footer(text = 'Nicklaus#5688 • Rename')

            await edit.edit(embed = embed)
            await ctx.message.clear_reactions()
            await ctx.message.add_reaction('✅')
        except discord.errors.Forbidden:
            embed = discord.Embed(
                title = 'Forbidden',
                description = "Uh oh, it seems I can't perform this action due to my permission levels.",
                color = discord.Color.red() # 0x06c9ff
            )
            embed.set_footer(text = 'Nicklaus#56880 • Rename')

            await ctx.reply(embed = embed)
            await ctx.message.add_reaction('❎')

async def setup(bot):
    await bot.add_cog(Rename(bot))
