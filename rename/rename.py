import discord
from discord.ext import commands
from core import checks

class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.thread_only()

    @commands.Cog.listener()
    async def on_command_error(ctx):
        await ctx.reply(embed = discord.Embed(
            description = 'Sorry, but it seems I have been rate limited.',
            color = 0x06c9ff
        ))
        await ctx.message.add_reaction('❎')

    @commands.command()
    async def rename(self, ctx, *, request):
        if not request:
            await ctx.reply(embed = discord.Embed(
                description = "Sorry, but it seems like you forgot to add a <request> argument.",
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')
            return

        try:
            await ctx.channel.edit(name = request)
            await ctx.message.add_reaction('✅')
            return
        except discord.errors.Forbidden:
            await ctx.reply(embed = discord.Embed(
                description = "Sorry, but it seems I can't perform this action due to my permission levels.",
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')
            return
        except discord.errors.RateLimited:
            await ctx.reply(embed = discord.Embed(
                description = 'Sorry, but it seems I have been rate limited.',
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')
            return
        except:
            await ctx.reply(embed = discord.Embed(
                description = 'An unexpected error occurred.',
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')
            return

async def setup(bot):
    await bot.add_cog(Rename(bot))
