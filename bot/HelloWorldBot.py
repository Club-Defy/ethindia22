# This example requires the 'message_content' intent.

import discord

class HelloWorldBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(f'Message from {message.author.id}: {message.content}')
        return await message.channel.send("bengali much?")
        # return await message.reference.send_message(f"only you, {message.user}, can see this!", ephemeral=True)


intents = discord.Intents.default()
intents.message_content = True

client = HelloWorldBot(intents=intents)
client.run('<token>')
