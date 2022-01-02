# Leah
# Written by aquova, 2022
# https://github.com/aquova/leah

import discord
from config import client, DISCORD_KEY, ART_CHANS, VERIFY_CHAN, GALLERY_CHAN

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id != VERIFY_CHAN or client.user != reaction.message.author:
        return
    txt = reaction.message.content.split('\n')
    embed = discord.Embed(title=f"Some amazing art by {str(user)}", type="rich", color=user.color, description=txt[-2])
    embed.set_image(url=txt[-1])
    gallery = client.get_channel(GALLERY_CHAN)
    await gallery.send(embed=embed)

@client.event
async def on_message(message):
    # Ignore all bots
    if message.author.bot:
        return

    if message.channel.id in ART_CHANS:
        verify = client.get_channel(VERIFY_CHAN)
        for img in message.attachments:
            await verify.send(f"<@{message.author.id}> has posted:\n{message.content}\n{img.url}")

client.run(DISCORD_KEY)