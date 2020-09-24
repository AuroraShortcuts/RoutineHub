from discord.ext import commands
import discord
import util
import os

client = commands.Bot(command_prefix = "-")

for f in os.listdir("./ext"):
	if f.endswith(".py"):
		client.load_extension("ext." + f[:-3])

@client.command()
@util.manage_bot()
async def reload(ctx):
	for f in os.listdir("./ext"):
		if f.endswith(".py"):
			client.unload_extension("ext." + f[:-3])
			client.load_extension("ext." + f[:-3])

	embed = discord.Embed(title = "Reload Complete", description = f"Reloaded all extensions.", color = discord.Color.green())
	await ctx.send(embed = embed)


token = ""
with open("token.txt", "r") as t:
	token = t.read()

client.run(token)
