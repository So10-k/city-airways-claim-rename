import discord
from discord.ext import commands

class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_plugins_ready(self, thread):
        await thread.reply(embed = discord.Embed(
        description = "Sorry, but it seems like you forgot to add a <request> argument.",
        color = 0x06c9ff
    ))

    @commands.command()
    async def rename(self, ctx, *, request):
        if not request:
            await ctx.reply(embed = discord.Embed(
                description = "Sorry, but it seems like you forgot to add a <request> argument.",
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')

        try:
            await ctx.channel.edit(name = request)
            await ctx.message.add_reaction('✅')
        except discord.errors.Forbidden:
            await ctx.reply(embed = discord.Embed(
                description = "Sorry, but it seems I can't perform this action due to my permission levels.",
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')
        except discord.errors.RateLimited:
            await ctx.reply(embed = discord.Embed(
                description = 'Sorry, but it seems I have been rate limited.',
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')
        except:
            await ctx.reply(embed = discord.Embed(
                description = 'An unexpected error occurred.',
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')

async def setup(bot):
    await bot.add_cog(Rename(bot))
