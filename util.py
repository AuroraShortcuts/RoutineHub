from discord.ext import commands

def manage_bot():
	roles = [504260053331869707, 506505954116763657]

	async def predicate(ctx):
		return [role.id in roles for role in ctx.author.roles] or ctx.author.id == 358425174837559297

	return commands.check(predicate)
