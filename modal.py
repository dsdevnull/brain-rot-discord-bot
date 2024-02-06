import disnake
from disnake.ext import commands
from disnake import TextInputStyle
import download


class MyModal(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Submit YouTube Link",
                placeholder="https://www.youtube.com/watch?--------",
                custom_id="name",
                style=TextInputStyle.short,
                max_length=50,
            )
        ]
        super().__init__(title="Create Tag", timeout=60, components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        # Manipulate the provided strings here
        await inter.response.defer()

        name = inter.text_values.get("name", "")

        if await download.getDownloadedAudio(name, inter):
            # Respond to the user (without embedding the input)
            await inter.edit_original_message(content=f"Received Video: Name = {name}")
        else:
            await inter.edit_original_message(
                content=f"Video '{name}' is age-restricted and cannot be downloaded."
            )
