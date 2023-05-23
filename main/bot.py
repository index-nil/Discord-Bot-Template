import discord
from discord import app_commands

guildId = None
token = None

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=guildId))
            self.synced = True
        print(f"{self.user} is now on-line on Discord.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=guildId), name = 'ping', description='Pong!')
async def ping(ctx: discord.Interaction):
    response = ctx.response
    await response.send_message(f"Pong!", ephemeral = True) 

aclient.run(token)