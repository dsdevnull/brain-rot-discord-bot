# brain-rot-discord-bot

This is a bot that will convert youtube links into MP3s for playback in a discord voice channel. This was created to have fun in dicord voice channels, add it to your gaming discord server!

Written in Python 3.12

You will need to have FFmpeg which can be downloaded from here: https://ffmpeg.org
This library is for audio processing, so it will need to be available on your path.

On Mac I recommend using `homebrew` for the installation since it does that work for you. `homebrew` is a package management software tool for MacOS. Follow the installation instructions for both Windows and Linux.

## Slash Commands:

- `/tags`: On command a modal will appear prompting the user to input a Youtube Link. This command will do the audio extraction and save the MP3 to the `sound` directory in the repo.
- `/play`: Upon using this command a list of all the available audio sources will appear for the user to select from. The user can either type out the sound, or selet the sound with their cursor.

## Future Work:

- Extract the audio sources from the repo. Currently, the audio sounds will only exisit on the users computer, this decision was made in order to ensure the repo would not be bloated from dozens of audio sources. Eventually I would like to store the sounds in an S3 bucket to be retrieved and store the S3 links in a Postgres table. That way there is a centralized sound source -- would require some rework of the functionality.
- Host the bot on a server, this would avoid the problems that might come up with the above proposed work. This could allow audio sources to be stored in one location, this would require turning the bot from a gateway bot to a POST bot (I think that is the term used by discord).

## Installation:

After installing FFmpeg:
`pip install .`

I recommand using an venv to run all python programs.
