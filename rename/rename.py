import discord
from discord.ext import commands
from core import checks

class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.thread_only()

    @commands.cooldown(2, 5, commands.BucketType.channel)

    @commands.command()
    async def rename(self, ctx, *, request):
        try:
            await ctx.channel.edit(name = request)
            await ctx.message.add_reaction('✅')
        except discord.errors.Forbidden:
            await ctx.reply(embed = discord.Embed(
                description = "Sorry, but it seems I can't perform this action due to my permission levels.",
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')
        
    @rename.error()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(embed = discord.Embed(
                description = 'Sorry, but it seems I have been rate limited.',
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')
        else:
            await ctx.reply(embed = discord.Embed(
                description = 'An unexpected error occurred. It has been logged to the bot console.\n\n```py\n' + str(error) + '```',
                color = 0x06c9ff
            ))
            await ctx.message.add_reaction('❎')

            raise error

async def setup(bot):
    await bot.add_cog(Rename(bot))
