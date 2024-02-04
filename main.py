import os
import asyncio
import disnake
import modal
import glob
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

mp3_options = glob.glob("sound/*.mp3")


intents = disnake.Intents.default()
intents.message_content = True

command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

bot = commands.Bot(
    command_prefix="!", intents=intents, command_sync_flags=command_sync_flags
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print(mp3_options)


async def autocomp_langs(inter: disnake.ApplicationCommandInteraction, user_input: str):
    mp3_options = glob.glob("sound/*.mp3")
    return [mp3 for mp3 in mp3_options if user_input.lower() in mp3]


@bot.slash_command(description="Play an MP3 file")
async def play(
    inter: disnake.ApplicationCommandInteraction,
    sound: str = commands.Param(autocomplete=autocomp_langs),
):
    # Get the voice channel where the user is connected
    voice_channel = inter.author.voice.channel
    if not voice_channel:
        await inter.response.send_message("You are not in a voice channel.")
        return

    # Connect to the voice channel
    vc = await voice_channel.connect()

    mp3_file_path = f"./{sound}"
    vc.play(disnake.FFmpegOpusAudio(mp3_file_path))

    # Wait until the audio finishes playing
    while vc.is_playing():
        await asyncio.sleep(0.25)

    # Disconnect from the voice channel
    await vc.disconnect()


@bot.slash_command()
async def tags(inter: disnake.AppCmdInter):
    """Sends a Modal to create a tag."""
    await inter.response.send_modal(modal=modal.MyModal())


bot.run(TOKEN)
