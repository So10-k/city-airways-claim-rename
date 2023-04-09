import discord
from discord.ext import commands
from core import checks

class Rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.thread_only()

    @commands.Cog.listener()
    async def cog_command_error(self, context, exception):
        if isinstance(exception, commands.CommandOnCooldown):
            await context.reply(embed = discord.Embed(
                description = 'Sorry, but it seems I have been rate limited.',
                color = 0x06c9ff
            ))
            await context.message.add_reaction('❎')
        else:
            await context.reply(embed = discord.Embed(
                description = 'An unexpected error occurred. It has been logged to the bot console.\n\n```py\n' + str(exception) + '```',
                color = 0x06c9ff
            ))
            await context.message.add_reaction('❎')

            raise exception

    @commands.cooldown(2, 5, commands.BucketType.user)

    @commands.command()
    async def rename(self, ctx, *, request):
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

async def setup(bot):
    await bot.add_cog(Rename(bot))
