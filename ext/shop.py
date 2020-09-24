from discord.ext import commands
import discord

class ShopCog(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["store"])
	async def shop(self, ctx):
		embed = discord.Embed(title = "RoutineHub Shop", description = "Use the above link to access the RoutineHub shop.", url = "https://https://routinehub.storenvy.com/", color = discord.Color.green())
		await ctx.send(embed = embed)

def setup(client):
	client.add_cog(ShopCog(client))
