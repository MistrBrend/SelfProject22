import discord
from discord import FFmpegPCMAudio
import responses
import random
import asyncio
import youtube_dl

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA5MDIyNTQzNTU0MDk5NjI2Ng.GbQ-Lw.n4iUCw7O2BwxResL7aOUJLcA4N-1n7NVI5pI7A'
    intents = discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True  # enable voice state tracking
    client = discord.Client(intents=intents)

    async def play_music(message, url):
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect()
        with youtube_dl.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2)
            vc.play(source)
        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if message.content.startswith('!play'):
            url = message.content.split(' ')[1]
            await play_music(message, url)

        if user_message == 'join':
            # check if the user is in a voice channel
            if message.author.voice and message.author.voice.channel:
                channel = message.author.voice.channel
                voice_client = await channel.connect()

                # play intro sound
                source = FFmpegPCMAudio('./sounds/kahoot-djlunatique.com.mp3')
                voice_client.play(source)

                print(f'The bot has connected to {channel.name} voice channel.')
            else:
                await message.channel.send("You're not in a voice channel.")

        elif user_message == 'joinV':
            # replace with the actual channel ID
            channel_id = 1003797905435525170
            channel = client.get_channel(channel_id)
            if channel:
                voice_client = await channel.connect()

                # play intro sound
                source = FFmpegPCMAudio('./sounds/kahoot-djlunatique.com.mp3')
                voice_client.play(source)

                print(f'The bot has connected to {channel.name} voice channel.')
            else:
                await message.channel.send("Invalid channel ID.")
        elif user_message == 'leave':
            # check if the bot is in a voice channel
            if message.guild.voice_client:
                await message.guild.voice_client.disconnect()
                print('The bot has left the voice channel.')
            else:
                await message.channel.send("I'm not in a voice channel.")
        elif user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    async def send_random_message(channel):
        while True:
            randomNumber = random.uniform(0.01, 0.02)
            quotes = responses.quotes
            jokes = responses.jokes
            tags = responses.tags

            quote = random.choice(quotes)
            joke = random.choice(jokes)
            tag = random.choice(tags)

            array_QJ = [quote, joke]

            random_array_QJ = random.choice(array_QJ)

            role_id = 1015016350827151451  # Replace with the role ID
            role_mention = f'<@&{role_id}>'

            await channel.send(f"'Waarom ging <@289741164167561216> naar ClashGG? Hij wilde weten hoe je meer geld kunt verliezen!' - {role_mention} tate")
            await channel.send(f"<@289741164167561216> shut up, before i kick u in the nuts and put the lights off. {tag} {random_array_QJ}")
            await asyncio.sleep(200)

            print("top G -> sended a random message")

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

       

    client.run(TOKEN)