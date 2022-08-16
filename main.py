import disnake
import os
from disnake.ext import commands
from keep_alive import keep_alive

keep_alive()
TOKEN = os.environ["TOKEN"]

client = commands.Bot(command_prefix="!",intents = disnake.Intents.all(), help_command=None)

@client.event
async def on_ready():
    print("Entropy is ready!")
    await client.change_presence(status = disnake.Status.online,activity = disnake.Game("Creating Chaos..."))


@client.command()
async def language(ctx):
    channel = client.get_channel(1009068358869717034)
    await channel.send(ctx.guild.preffered_locale)

extensions = ["cogs.avatar"]

for extension in extensions:
    client.load_extension(extension)




client.i18n.load("localization/")
client.run(TOKEN)