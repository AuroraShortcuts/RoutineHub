from discord.ext import commands
import discord

class ErrorHandler(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CheckFailure):
			embed = discord.Embed(title = "Error", description = "You don't have permission to do this.", color = discord.Color.red())
			await ctx.send(embed = embed)

def setup(client):
	client.add_cog(ErrorHandler(client))
